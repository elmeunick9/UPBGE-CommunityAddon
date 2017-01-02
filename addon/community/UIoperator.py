from .macro import *
from . import utils

import bpy, os, shutil, platform, subprocess
from bpy.props import *

class NewGameProject(bpy.types.Operator):
	bl_idname = "wm.new_game_project"
	bl_label = "New Game Project"
	bl_options = {'REGISTER'}
	
	filepath = StringProperty(subtype='FILE_PATH')
	
	def execute(self, context):
		if os.path.exists(self.filepath):
			self.report({'ERROR_INVALID_INPUT'}, "Error creating new project," + self.filepath + " file or directory already exists.")
			return {'CANCELLED'}
		
		name = os.path.basename(self.filepath) 
		if name == "":
			 self.report({'ERROR_INVALID_INPUT'}, "Error creating new project, project name can not be empty.")
			 return {'CANCELLED'}
			
		tfolder = bpy.utils.user_resource('DATAFILES') + LIBNAME + os.sep + 'template' + os.sep
		shutil.copytree(tfolder, self.filepath)
		
		#Open the new blend
		bpy.ops.wm.open_mainfile(filepath=self.filepath + os.sep + 'project'  + os.sep + 'main.blend')
		
		utils.loadProjectFile(self.filepath + os.sep + 'project.json')
			
		return {'FINISHED'}
	
	def invoke(self, context, event):
		wm = context.window_manager
		wm.fileselect_add(self)
		return {'RUNNING_MODAL'}
	
	
class LoadGameProject(bpy.types.Operator):
	bl_idname = "wm.load_game_project"
	bl_label = "Load Game Project"
	bl_options = {'REGISTER'}
	
	filepath = StringProperty(subtype='FILE_PATH')
	
	def execute(self, context):
		name = os.path.basename(self.filepath)
		
		#TODO: put on another file and module
		
		def checkProjectFile(path):
			if os.path.basename(path) != "project.json": return False
			if not os.path.isfile(path): return False
				
			utils.loadProjectFile(path)
					
			if not 'bge-project' in utils.project_data: return False
				
			return True
				 
		def getMainBlend(path):
			path = os.path.dirname(path) + os.sep + "project" +  os.sep + "main.blend"
			if os.path.isfile(path): return path
		
		list=[self.filepath, self.filepath + "project.json", os.path.dirname(self.filepath) + os.sep + "project.json", os.path.dirname(self.filepath) + os.sep + "../" + "project.json"]
		
		endpath=None
		for path in list:
			if checkProjectFile(path): endpath=getMainBlend(path)
		
		if endpath==None:
			self.report({'ERROR_INVALID_INPUT'}, "Error loading project, project file not found.")
			return {'CANCELLED'}
	
		bpy.ops.wm.open_mainfile(filepath=endpath)
		return {'FINISHED'}
	
	def invoke(self, context, event):
		wm = context.window_manager
		wm.fileselect_add(self)
		return {'RUNNING_MODAL'}
		
class ExploreProjectDirectory(bpy.types.Operator):
	bl_idname = "wm.explore_project_directory"
	bl_label = "Load Game Project"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		path = os.path.dirname(bpy.data.filepath)
		if platform.system() == "Windows":
			os.startfile(path)
		elif platform.system() == "Darwin":
			subprocess.Popen(["open", path])
		else:
			subprocess.Popen(["xdg-open", path])
		
		return {'FINISHED'}
	
	
def register():
	bpy.utils.register_class(NewGameProject)
	bpy.utils.register_class(LoadGameProject)
	bpy.utils.register_class(ExploreProjectDirectory)
 
def unregister():
	bpy.utils.unregister_class(NewGameProject)
	bpy.utils.unregister_class(LoadGameProject)
	bpy.utils.unregister_class(ExploreProjectDirectory)