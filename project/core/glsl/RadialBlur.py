from filter2D import Filter2D

class  RadialBlur(Filter2D):
	""" Adds blur around the edges of the screen, useful for a running effect.
	
	.. image:: ../Filter2DImages/RadialBlur.jpg
	
	\\
	
	.. attribute:: radial_density
		
		:type: float
			
	"""
	
	radial_density = 0.05