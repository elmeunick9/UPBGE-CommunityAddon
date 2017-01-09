from filter2D import Filter2D

class Vignetting(Filter2D):
	"""
	
	Reduces the image's brightness or saturation at the periphery compared to the image center. Has configurable inner and outer color.
	
	.. image:: ../Filter2DImages/Vignetting.jpg
	
	\\
	
	.. attribute:: u_inner_color
		
		The RGB values of the inner color. Alpha chanel unused. Default: (1.0,1.0,1.0,0.0) 
		
		:type: vec4
	
	.. attribute:: u_outer_color
		
		The RGB values of the outer color. Default: (0.0,0.0,0.0) 
		
		:type: vec3
		
	.. attribute:: u_scale
	
		Default: 1.0
		
		:type: float
		
	.. attribute:: u_radius

		Outer radious, use together with scale to adjust the overall size and gradient. Default: 1.1
	
		:type: float
	
	.. attribute:: u_intensity
			
		Tweaks the intensity of the outer color. Default: 0.8

		:type: float
		
	.. attribute:: u_resolution
			
		The resolution of the screen, used for the shape and overall size. Default: [render.getWindowWidth(), render.getWindowHeight()]

		:type: vec2
	"""
	
	def __define__(self):
		""" You must only import bge modules here """
		from bge import render
		Vignetting.u_resolution = [render.getWindowWidth(), render.getWindowHeight()]
		
	
	u_inner_color=(1,1,1,0)
	u_outer_color=(0,0,0)
	u_scale = 1.0
	u_intensity = 0.8
	u_radius = 1.1