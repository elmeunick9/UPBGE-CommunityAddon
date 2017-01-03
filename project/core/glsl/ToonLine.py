from filter2D import Filter2D

class  ToonLine(Filter2D):
	""" Adds blur around the edges of the screen, useful for a running effect.
	
	.. image:: ../Filter2DImages/ToonLine.jpg
	
	\\
	
	.. attribute:: border_color

		The color of the edges.
	
		:type: Vec4
	
	.. attribute:: brightness
	
		General light, If you want black&white use mode 0 and a very hight light (e.j: 400)
		
		:type: float
		
	.. attribute:: mode

		If 0 the border won't be smoothed.
	
		:type: float
		
	.. attribute:: threshold
	
		:type: float
		
	"""
	
	brightness = 1.0
	border_color = [0.0, 0.0, 0.0, 0.0]
	mode = 1
	threshold = 0.3