import inspect, re
import bgl, bge

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
		self.shadow = None
		
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
		if not self.owner:
			from bge import logic
			self.owner = logic.getCurrentController().owner
			self.scene = self.owner.scene
			
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
		if self.scene == None: return
		self.scene.filterManager.removeFilter(self.slot)
		Filter2D.uslot.remove(self.slot)
		
	def __del__(self):
		try:
			name = self.__class__.__name__
			slot = self.slot
			self.unload()
			verbose("Removed 2D Filter " + name + " at slot " + str(slot))
		except SystemError: pass	
			
	def __setattr__(self, name, value):
		super().__setattr__(name, value)
		if name in self.uniforms:
			self.bindUniformf(name)
		
			
	def bindAllUnioforms(self):
		for uniform in self.uniforms:
			self.bindUniformf(uniform)
			
	def bindUniformf(self, name):
		t=self.__dict__[name]
		if type(t) in [list, tuple]: self.shader.setUniformfv(name, list(t))
		else: self.shader.setUniform1f(name, t)
		