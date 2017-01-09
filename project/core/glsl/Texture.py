from filter2D import Filter2D

class  Texture(Filter2D):
	""" Prints a texture on the screen, example on how to use sampler2D uniforms. 
	
	.. raw:: html
	
		<iframe width="560" height="315" src="https://www.youtube.com/embed/iiNVnp1Bo2c" frameborder="0" allowfullscreen></iframe>
		
	\\
	
	.. attribute:: opacity
		
		:type: float
		
	.. attribute:: texture
	
		:type: sampler2D
		
		
	"""
	
	def __define__(self):
		
		#We only want this to be accesible from Python.
		Texture.filter_color = [0.0,0.0,0.0,0.0]
		Texture.threshold = 0.05
		Texture.samples = 1
	
	texture = ""
	opacity = 1.0
	
