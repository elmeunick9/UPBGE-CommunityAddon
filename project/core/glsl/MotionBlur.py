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
		
	
		self.x0 = cameraMatrix[0][0]
		self.x1 = cameraMatrix[0][1]
		self.x2 = cameraMatrix[0][2]
		self.x3 = cameraMatrix[0][3]
		self.x4 = cameraMatrix[1][0]# + F
		self.x5 = cameraMatrix[1][1]
		self.x6 = cameraMatrix[1][2]# + S
		self.x7 = cameraMatrix[1][3]
		#self.x8 = cameraMatrix[2][0]# + T
		#self.x9 = cameraMatrix[2][1]
		#self.x10 = cameraMatrix[2][2]# + L
		#self.x11 = cameraMatrix[2][3]
		self.x12 = cameraMatrix[3][0]
		self.x13 = cameraMatrix[3][1]
		self.x14 = cameraMatrix[3][2]
		self.x15 = cameraMatrix[3][3]

		cameraMatrix = set.inverted()

		self.viewProjectionInverse = cameraMatrix

		own['prev'] = set