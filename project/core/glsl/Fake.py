from filter2D import Filter2D
from bge import logic
import inspect

class Fake():
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