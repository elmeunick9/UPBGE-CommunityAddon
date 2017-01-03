from filter2D import Filter2D
import time

class Drugged(Filter2D):
	""" Like if you've taken 800ug of LSD 
	
	.. image:: ../Filter2DImages/Drugged.jpg
	
	\\
	
	.. attribute:: contrast, brightness, amplitude, turbulence
		
		:type: float
		
	
	"""
	
	def load(self):
		super().load()
		self.scene.pre_draw.append(self.update)
	
	def unload(self):
		self.scene.pre_draw.remove(self.update)
		super.unload()
	
	#Initializes uniforms that won't show on the Blender UI.
	#Uniforms must be Class attributes, otherwise they will be taken as normal attributes.
	def __define__(self):
		self.t = time.time()
		Drugged.timer = self.t
	
	def update(self):
		self.timer = time.time() - self.t
		
	contrast = 1.8
	brightness = 0.8
	amplitude = 0.08
	turbulence = 20.0