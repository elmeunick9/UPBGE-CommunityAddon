from filter2D import Filter2D

class MotionBlur(Filter2D):
	"""
	Blur when in motion...
	
	.. image:: ../Filter2DImages/GameBoyColor.jpg
	
	\\
	
	"""
	
	distance = 0.2
	
	def __define__(self):
		self.own = {}
		self.update()
	
	def load(self):
		super().load()
		self.scene.pre_draw.append(self.update)
	
	def unload(self):
		self.scene.pre_draw.remove(self.update)
		super.unload()

		
	def update(self):
		from bge import logic as G
		import math

		scene = G.getCurrentScene()
		own = self.own

		cam = scene.active_camera
		wtc = cam.world_to_camera

		own['rota'] = math.degrees(cam.localOrientation.to_euler().x)

		if 'init' not in own:
			set = cam.projection_matrix * wtc
			own['prev'] = set
			own['init'] = True
			self = MotionBlur
		set = (cam.projection_matrix * wtc)
		cameraMatrix = own['prev']
		
		self.x = cameraMatrix
		self.viewProjectionInverse = set.inverted()

		own['prev'] = set