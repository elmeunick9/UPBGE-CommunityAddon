from .macro import *
from .UIoperator import *
from . import utils

import bpy
import bpy.props as prop

class ProjectMenu(bpy.types.Menu):
	bl_label = "Project"
	bl_idname = "INFO_MT_project"

	def draw(self, context):
		self.layout.operator(NewGameProject.bl_idname,  text="New Game Project", icon='NEW')
		self.layout.operator(LoadGameProject.bl_idname, text="Load Game Project", icon='FILE_FOLDER')
		if utils.project_data != None:
			self.layout.operator(ExploreProjectDirectory.bl_idname, text="Explore Project Directory", icon='FILE_FOLDER')
			self.layout.operator(SaveProjectAs.bl_idname, text="Save Project As ...", icon='SAVE_AS')
		
def fileMenuDraw(self, context):
	
	self.layout.menu("INFO_MT_project")

	
def register():
	bpy.utils.register_class(ProjectMenu)
	bpy.types.INFO_MT_file.prepend(fileMenuDraw)
	
def unregister():
	bpy.utils.unregister_class(ProjectMenu)
	bpy.types.INFO_MT_file.remove(fileMenuDraw)
