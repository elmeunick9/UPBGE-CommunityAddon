import bge, mathutils
from collections import OrderedDict

#If false, we don't have blender avaliable.
with_bpy = False
try:
	import bpy
	if str(type(bge)) != "<class 'sphinx.ext.autodoc._MockModule'>":
		with_bpy = True
except Exception: pass
	
class ThirdPerson(bge.types.KX_PythonComponent):
	""" Third Person controls. WASD to move and space to jump (with inhertia).
	
	.. attribute:: move_speed
	
		The movement on the WS.
	
	.. attribute:: turn_speed
		
		The movement on the AD.
	
	.. attribute:: jump_force
	
		The movement on the SPACE
	
	"""

	args = OrderedDict([
		("Move Speed", 0.1),
		("Turn Speed", 0.04),
		("Jump Force", 250),
	])

	def start(self, args):
		self.move_speed = args['Move Speed']
		self.turn_speed = args['Turn Speed']
		
		self.object.collisionCallbacks.append(self.collide)
		self.collision_time = 0
		self.jump_force = args["Jump Force"]
		self.inertia = 0
		
	def update(self):
		ACTIVE = bge.logic.KX_INPUT_ACTIVE
		W_KEY = bge.logic.keyboard.inputs[bge.events.WKEY].status[0] == ACTIVE
		S_KEY = bge.logic.keyboard.inputs[bge.events.SKEY].status[0] == ACTIVE
		A_KEY = bge.logic.keyboard.inputs[bge.events.AKEY].status[0] == ACTIVE
		D_KEY = bge.logic.keyboard.inputs[bge.events.DKEY].status[0] == ACTIVE
		SPACE_KEY = bge.logic.keyboard.inputs[bge.events.SPACEKEY].status[0] == ACTIVE
	
		move = 0
		rotate = 0
			
		if W_KEY: move += self.move_speed
		if S_KEY: move -= self.move_speed
		if A_KEY: rotate += self.turn_speed
		if D_KEY: rotate -= self.turn_speed
		
		#Jump only when not touching the ground, the more time you press the key the higher you jump
		if SPACE_KEY and self.collision_time > 0: self.object.applyForce((0,0, self.jump_force/self.collision_time))
		
		#Movmenet on air is reduced, but not nullified.
		e = 0.01
		if self.collision_time > 0:
			self.collision_time -= 1
			e = 1
		else:
			rotate /= 5
		move = move*e + self.inertia*(1-e)
		
		self.inertia = move
		self.object.applyMovement((0, move, 0), True)
		self.object.applyRotation((0, 0, rotate), True)
		
	def collide(self, object, point, normal):
		from bge import render
	
		#Normal used to fall on clifs.
		if normal.z < -0.5:
			self.collision_time = 5
			#d = mathutils.Vector((normal.x, normal.y, -normal.z))
			#d.length = -normal.z*9.8
			#print(1+normal.z)
			#self.object.applyForce(d)
			
			#render.drawLine(self.object.worldPosition, self.object.worldPosition + d, [1,0,0,1])
		
		
class MouseLook(bge.types.KX_PythonComponent):
	""" Mouselook to be used with a camera.
	
	You can control the camera orientation with the mouse and move arround with WASD.

	.. attribute:: sensitivity
	
		The sensitivity of the mouse. *Default: 0.75*
		
	.. attribute:: deathzone
	
		The amount of mouse movement that will be considered noise. Default: 0.002
		
	.. attribute:: invertx, inverty
	
		Mouse invert, 1 or -1
	
	.. attribute:: speedx
	
		The speed of movement on the x axis. (Left/Right) *Default: 0.1*
	
	.. attribute:: speedz
	
		The speed of movement on the z axis. (Front/Back) *Default: 0.3*
	
	.. attribute:: angle
	
		It can be used to ensure a maixum rotation on the x axis, so avoiding an inverted view. Smaller than 0, no limit will be applied, otherwise a float representing the angle in radiants (for one direction) will be used. *Default: 1*
		
	.. attribute:: continuous
	
		If true the mouse won't be setted to the (0.5, 0.5) position.
	
	
	"""

	args = OrderedDict([
		("Sensitivity", 0.75),
		("Invert X", False),
		("Invert Y", False),
		("Speed X", 0.1),
		("Speed Z", 0.3),
		("Angle", 1.0),
		("Continuous", False),
	])

	def start(self, args):
		self.sensitivity = args['Sensitivity']
		self.deathzone = 0.002
		self.invertx = 1 if args["Invert X"] else -1
		self.inverty = 1 if args["Invert Y"] else -1
		self.speedx = args["Speed X"]
		self.speedz = args["Speed Z"]
		self.lock_rotation = args["Angle"]
		self.continuous = args["Continuous"]
		
		bge.logic.mouse.position = (0.5, 0.5)

	def update(self):		
		#---- MouseLook ----
		x, y = bge.logic.mouse.position
		tmp = self.object.localOrientation.to_euler()
		rot = tmp.copy()
		xdif = (y-0.5)*self.inverty*self.sensitivity
		zdif = (x-0.5)*self.invertx*self.sensitivity
		deathzone = self.deathzone if not self.continuous else self.deathzone/8
		
		if abs(xdif) > deathzone: tmp.x += xdif
		if abs(zdif) > deathzone: tmp.z += zdif
		if self.lock_rotation < 0: rot = tmp
		else:
			rot.z = tmp.z
			if abs(tmp.x-1.57) <= self.lock_rotation:
				rot.x = tmp.x
		
		self.object.localOrientation = rot
		if not self.continuous: bge.logic.mouse.position = (0.5, 0.5)
		
		#---- Movement ----
		ACTIVE = bge.logic.KX_INPUT_ACTIVE
		W_KEY = bge.logic.keyboard.inputs[bge.events.WKEY].status[0] == ACTIVE
		S_KEY = bge.logic.keyboard.inputs[bge.events.SKEY].status[0] == ACTIVE
		A_KEY = bge.logic.keyboard.inputs[bge.events.AKEY].status[0] == ACTIVE
		D_KEY = bge.logic.keyboard.inputs[bge.events.DKEY].status[0] == ACTIVE

		m = [0,0,0]
		if W_KEY: m[2] = -self.speedz
		if S_KEY: m[2] = +self.speedz
		if A_KEY: m[0] = -self.speedx
		if D_KEY: m[0] = +self.speedx
		if m != [0,0,0]: self.object.applyMovement(m, True)
		
		
#HERE BE DRAGONS
camera_zoom = None
if with_bpy:
	for area in bpy.context.screen.areas:
		if area.type == 'VIEW_3D':
			camera_zoom = area.spaces.active.region_3d.view_distance
	
	
class View3D(bge.types.KX_PythonComponent):
	""" Navigate just like in Blender, to be used with a camera. """

	args = OrderedDict([
		("Camera Zoom", camera_zoom if camera_zoom else 10),
	])

	def start(self, args):
		if with_bpy:
			components = bpy.data.objects[self.object.name].game.components
			components["View3D"].properties["Camera Zoom"].value = camera_zoom
			
		self.old_mouse = bge.logic.mouse.position
		self.camera_zoom = camera_zoom if camera_zoom else args["Camera Zoom"]

	def update(self):		
		ACTIVE = bge.logic.KX_INPUT_ACTIVE
		x, y = bge.logic.mouse.position
		
		MIDDLE_KEY = bge.logic.mouse.inputs[bge.events.MIDDLEMOUSE].status[0] == ACTIVE
		CTRL_KEY = bge.logic.keyboard.inputs[bge.events.LEFTCTRLKEY].status[0] == ACTIVE
		SHIFT_KEY = bge.logic.keyboard.inputs[bge.events.LEFTSHIFTKEY].status[0] == ACTIVE
		
		wup = 1 if bge.logic.mouse.inputs[bge.events.WHEELUPMOUSE].status[0] == ACTIVE else 0
		wdw = 1 if bge.logic.mouse.inputs[bge.events.WHEELDOWNMOUSE].status[0] == ACTIVE else 0
		wheel = wup - wdw
		
		
		if MIDDLE_KEY:
			ox, oy = self.old_mouse
			xdif = (oy-y)*3
			zdif = (ox-x)*3
			
			if SHIFT_KEY:
				m=[0,0,0]
				m[1] = -xdif*self.camera_zoom/3
				m[0] = zdif*self.camera_zoom/3
				self.object.applyMovement(m, True)
			
			elif CTRL_KEY:
				d = xdif+zdif
				wheel = d
				
			else:
				tmp = self.object.worldOrientation.to_euler()
				rot = tmp.copy()
				
				d = self.camera_zoom
				
				if abs(xdif) < 0.2: tmp.x += xdif
				if abs(zdif) < 0.2: tmp.z += zdif
				self.object.localOrientation = tmp
				
				vdist = mathutils.Vector((0, 0, d))
				v = vdist.copy()
				v.rotate(rot)
				origin = self.object.worldPosition - v
				v = vdist.copy()
				v.rotate(tmp)
				final = origin + v
			
				self.object.worldPosition = final
				
				
		if wheel != 0:
			wf = wheel * self.camera_zoom/5
			rot = self.object.worldOrientation.to_euler()
			v = mathutils.Vector((0, 0, -wf))
			v.rotate(rot)
			self.object.worldPosition = v + self.object.worldPosition
			
			self.camera_zoom -= wf
		
		self.old_mouse = x, y
		
			
				
		

