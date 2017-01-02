import sys, os
sys.path.append(os.path.join(sys.path[0],'core','glsl', '__global__'))

import pkgutil
import inspect

__all__ = []

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
	module = loader.find_module(name).load_module(name)

	for name, value in inspect.getmembers(module):
		if name.startswith('__'):
			continue
			
		globals()[name] = value
		__all__.append(name)
	
