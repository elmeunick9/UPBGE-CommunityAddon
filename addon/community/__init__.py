bl_info = {
    "name": "Community Addon",
    "author": "Robert Planas (elmeunick9)",
    "location": "File >> New Project",
    "category": "Game Engine",
    "blender": (2, 73, 0),
    "description": "An UPBGE Framework."
}

from .macro import *

if "bpy" in locals():
    import imp
    imp.reload(install)
    imp.reload(utils)
else:
    from . import install, utils

import bpy 

from bpy.app.handlers import persistent

@persistent
def scene_loaded(dummy):
	
	#Check if this is a newer installation & install if nesscesary.
	install.check()
	
modulesNames = ['UIdraw', 'UIoperator', 'UIshader', "game_project_export"]
 
modulesFullNames = []
for currentModuleName in modulesNames:
	modulesFullNames.append('{}.{}'.format(__name__, currentModuleName))
 
import sys
import importlib
 
for currentModuleName in modulesFullNames:
	if currentModuleName in sys.modules:
		importlib.reload(sys.modules[currentModuleName])
	else:
		globals()[currentModuleName] = importlib.import_module(currentModuleName)
 
def register():
	for currentModuleName in modulesFullNames:
		if currentModuleName in sys.modules:
			if hasattr(sys.modules[currentModuleName], 'register'):
				sys.modules[currentModuleName].register()
	
	bpy.app.handlers.load_post.append(scene_loaded)
	bpy.app.handlers.game_pre.append(utils.checkForLaunch)
	bpy.app.handlers.save_pre.append(utils.checkForLaunch)
	
	install.check()
 
def unregister():
	for currentModuleName in modulesFullNames:
		if currentModuleName in sys.modules:
			if hasattr(sys.modules[currentModuleName], 'unregister'):
				sys.modules[currentModuleName].unregister()
	
	bpy.app.handlers.game_pre.remove(utils.checkForLaunch)
	bpy.app.handlers.save_pre.remove(utils.checkForLaunch)
	#install.uninstall()
	
if __name__ == "__main__":
	register()
	
install.check()