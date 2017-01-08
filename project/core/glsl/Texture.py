from filter2D import Filter2D

class  Texture(Filter2D):
	""" Prints a texture on the screen
	
	.. attribute:: opacity
		
		:type: float
		
	.. attribute:: texture
	
		:type: sampler2D
		
	"""
	
	texture = ""
	opacity = 1.0