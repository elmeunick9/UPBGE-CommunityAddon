import inspect, re, os
import bgl, bge, mathutils

#######################################
try:
	from script import constant
except:
	class constant:
		CORE_DEBUG_PRINT = True
		CORE_DEBUG_VERBOSE = True

def debug(text):
	if constant.CORE_DEBUG_PRINT == True: print(text)

def verbose(text):
	if constant.CORE_DEBUG_VERBOSE == True: print(text)
	
def newTextureFromFile(path):
	""" Input a filepath of an image, create the texture with BGL and return its bindID """
	imagePath = path
	image = bge.texture.ImageFFmpeg(imagePath)
	return [image, newTextureFromBuffer(image.image, image.size[0], image.size[1])]
	
def newTextureFromBuffer(buffer, sizex, sizey, id_buf=None):
	""" Returns a bgl.Buffer of one element containing the bindID """
	
	#Generate new texture
	if id_buf == None:
		id_buf = bgl.Buffer(bgl.GL_INT, 1)
		bgl.glGenTextures(1, id_buf)
	
	#Steup and bind texture
	bgl.glBindTexture(bgl.GL_TEXTURE_2D, id_buf[0])
	bgl.glTexImage2D(bgl.GL_TEXTURE_2D, 0, bgl.GL_RGBA, sizex, sizey, 0, bgl.GL_RGBA, bgl.GL_UNSIGNED_BYTE, buffer)
	bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_LINEAR);
	bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_LINEAR);

	return id_buf #bindID // bindCode
	
class Filter2D():

	scene = None
	owner = None
	slot = None
	uslot = []
	
	def __init__(self, **kw):
		#Class attributes from children classes will be considered as uniforms,
		#they will also be accesed as instance attributes,
		#the uniform will be updated when an instance attribute that is also uniform is.
	
		self.uniforms = []
		self.textures = []
		
		if not self.owner:
			from bge import logic
			self.owner = logic.getCurrentController().owner
			self.scene = self.owner.scene
		
		self.__define__() #For child
	
		#Make child class attributtes become instance attributtes.
		for key, value in self.__class__.__dict__.items():
			if key.startswith('__'): continue
			if inspect.ismethod(getattr(self.__class__, key)): continue
			if inspect.isfunction(getattr(self.__class__, key)): continue
			
			self.__dict__[key] = value
			self.uniforms.append(key)
			
		#Make list of kw become instance attributes, override current attributes.
		self.__dict__.update(kw)
		
		self.load()
		
	def __define__(self): pass
			
	def load(self):
		from bge import logic
		
		if self.slot == None:
			try: self.slot = max(Filter2D.uslot)+1
			except ValueError: self.slot = 0
			Filter2D.uslot.append(self.slot)
		else:
			if self.slot in Filter2D.uslot:
				raise ValueError("Filter2D slot already in use")
				
		#Remove uniforms that are properties
		self.uniforms = [x for x in self.uniforms if x not in self.owner.getPropertyNames()]
				
		#Setup the shader
		try:
			#Components nescesary to setup the shader.
			name = self.__class__.__name__
		
			owner = self.owner
			slot = self.slot

			path = logic.expandPath("//core/glsl/" + name + ".filter2D")
			with open(path, "r") as input:
				text = input.read()

			self.scene.filterManager.addFilter(slot, bge.logic.RAS_2DFILTER_CUSTOMFILTER, text)
			self.shader = self.scene.filterManager.getFilter(slot)
			
			self.bindAllUnioforms()		
			
			verbose("Setted 2D Filter " + name + " to slot " + str(slot))
		
		except:
			import traceback
			traceback.print_exc()

	def unload(self):
		if self.scene != None:
			try: self.scene.filterManager.removeFilter(self.slot)
			except SystemError: pass
			Filter2D.uslot.remove(self.slot)
		for x in self.textures:
			if str(type(x)) == "<class 'bgl.Buffer'>": bgl.glDeleteTextures(1,  x)
		
	def __del__(self):
		name = self.__class__.__name__
		slot = self.slot
		self.unload()
		verbose("Removed 2D Filter " + name + " at slot " + str(slot))
			
	def __setattr__(self, name, value):
		super().__setattr__(name, value)
		if name in self.uniforms:
			self.bindUniformf(name)
		
	def bindAllUnioforms(self):
		for uniform in self.uniforms:
			try:
				self.bindUniformf(uniform)
			except RuntimeWarning: continue
			
	def bindSampler2D(self, name, bindID, slot=0):
		bgl.glActiveTexture(bgl.GL_TEXTURE0 + bindID)
		bgl.glBindTexture(bgl.GL_TEXTURE_2D, bindID)
		self.shader.setTexture(slot, bindID, name)
		self.shader.setSampler(name, slot)
		
	def bindUniformf(self, name):
	
		t=self.__dict__[name]
			
		#Check if it's texture
		if type(t) == str:
			if not os.path.isabs(t): t = bge.logic.expandPath('//' + t)
			image, buf_id = newTextureFromFile(t)
			if not buf_id in self.textures: self.textures.append(buf_id)
			self.bindSampler2D(name, buf_id[0], self.textures.index(buf_id))
			return
			
		if str(type(t)) == "<class 'BL_Texture'>":
			if not t.bindCode in self.textures: self.textures.append(t.bindCode)
			self.bindSampler2D(name, t.bindCode, self.textures.index(t.bindCode))
			return
			
		if str(type(t)) == "<class 'VideoTexture.Texture'>":
			if not t.bindId in self.textures: self.textures.append(t.bindId)
			self.bindSampler2D(name, t.bindId, self.textures.index(t.bindId))
			return
		
		if type(t) == tuple and len(t) == 3:
			buff, sx, sy = t 
			if str(type(buff)) == "<class 'bgl.Buffer'>":
				buf_id = newTextureFromBuffer(buff, sx, sy)
				if not buf_id in self.textures: self.textures.append(buf_id)
				self.bindSampler2D(name, buf_id[0], self.textures.index(buf_id))
				return
				
		if type(t) == tuple and len(t) == 2:
			code, bindId = t 
			if code == "bindCode" or code == "bindId" or code == "bindID":
				if not bindId in self.textures: self.textures.append(bindId)
				self.bindSampler2D(name, bindId, self.textures.index(bindId))
				return
			
		
		#Check if it's int/float or vecX/matX
		if type(t) in [list, tuple, mathutils.Matrix, mathutils.Vector]:
			if len(t) == 0: raise RuntimeWarning("Uniform vec3 or vec4" + name + " malformed, it's empty.")
			
			#Check if it's vecX or matX
			if type(t[0]) in [list, tuple, mathutils.Matrix, mathutils.Vector]:
			
				if len(t) == 3:
					if len(t[0]) != 3 or len(t[1]) != 3 or len(t[2]) != 3:
						raise RuntimeWarning("Uniform mat3 " + name + " malformed")
					self.shader.setUniformMatrix3(name, t.transposed())
					
				elif len(t) == 4:
					if len(t[0]) != 4 or len(t[1]) != 4 or len(t[2]) != 4 or len(t[3]) != 4:
						raise RuntimeWarning("Uniform mat4 " + name + " malformed")
					self.shader.setUniformMatrix4(name, t.transposed())
					
				else: raise RuntimeWarning("Uniform mat3 or mat4 malformed, size " + len(t))
				
			#It's a VecX
			else:
				self.shader.setUniformfv(name, list(t))
				
		#It's an int/float
		else:
			try:
				if type(t) == int: self.shader.setUniform1i(name, t)
				else: self.shader.setUniform1f(name, t)
			except TypeError:
				print("TypeError on uniform", name, "of type", type(t))
		