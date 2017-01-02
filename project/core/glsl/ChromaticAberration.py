from filter2D import Filter2D

class ChromaticAberration(Filter2D):
	"""
	
	Lents effect, makes the image look blurred with colored edges with the fect being increased at the borders of the screen.
	
	.. attribute:: displacement
		
		The amount of displacemnet (intensity of the effect). Default: 1 
		
		:type: float
	"""
	
	displacement = 0.6