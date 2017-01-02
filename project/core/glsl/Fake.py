from filter2D import Filter2D
from bge import logic
import inspect

class Fake():

	""" A fake filter2D. It works diferent to the other shaders as it's not a subclass of Filter2D. Used to fake an existing filter so that you can dishable a filter without touching a lot of code. Example:
	
	.. code-block:: python
	
		if use_vignetting: self.vignetting = utils.filter2d.Vignetting()
		else: self.vignetting = utils.filter2d.Fake(utils.filter2d.Vignetting)
		self.vignetting.colorR = 0.5 #Doesn't rise exception even with ``use_vignetting == False``
	
	"""

	
	owner = None
	slot = None
	
	def __init__(self, Class):
		self.uniforms = []
		self.program = None
		self.error = 0
		
		for key, value in Class.__dict__.items() :
			if key.startswith('__'): continue
			if inspect.ismethod(getattr(Class, key)): continue
			if inspect.isfunction(getattr(Class, key)): continue
			
			self.__dict__[key] = value
			self.uniforms.append(key)
	
		if not self.owner:
			from bge import logic
			self.owner = logic.getCurrentController().owner
			
		self.uniforms = [x for x in self.uniforms if x not in self.owner.getPropertyNames()]