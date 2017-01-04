from .macro import *
from . import utils

import bpy, os, shutil, platform
from bpy.props import *

import time

class ExportGameProject(bpy.types.Operator):
	bl_idname = "wm.export_game_project"
	bl_label = "Export Game Project"
	
	platform = EnumProperty(
		name="Platform",
		items=(('WIN32', "Windows-32", "Windows 32-bit (Recomended for: XP, Vista, 7)"),
			   ('WIN64', "Windows-64", "Windows 64-bit (Recomended for: 8, 10)"),
			   ('LIN32', "Linux-32", "Linux 32-bit"),
			   ('LIN64', "Linux-64", "Linux 64-bit"),
			   ('MACOS', "MacOS", "Not properly tested"),
			   ),
		options={'ENUM_FLAG'},
		default={utils.getPlatformCode()},
		)
		
	output_path = StringProperty(name="Output", subtype="DIR_PATH", default="release/", description="The folder where you're going export the game")

	def execute(self, context):
		tfolder = os.path.dirname(bpy.data.filepath) + os.sep
		game_name = os.path.basename(os.path.normpath(tfolder + "../"))
		my_platform = str(self.platform)[2:-2]
		out = os.path.normpath(tfolder + ".." + os.sep + self.output_path) + os.sep if not os.path.isabs(self.output_path) else self.output_path
		
		#Clean the way
		try:
			if os.path.isdir(out): shutil.rmtree(out)
		except PermissionError:
			self.report({'ERROR'}, "Permission Error on output directory")
			return {'CANCELLED'}
		
		#Copy Project
		def fileignore(file):
			list = [".blend1", ".blend2", ".blend3", ".blend4", ".blend5", ".pyc", "ehthumbs.db", "~", "__pycache__"]
			for l in list:
				if file.endswith(l): return True
			

		start_time = time.time()
		def prog(x):
			print(x)
			if time.time() > start_time + 5: return False #Should be true
			
		
		utils.copytree(tfolder, out + "data" + os.sep, fileignore, prog)
		shutil.copyfile(tfolder + ".." + os.sep + "project.json", out + "project.json")
		
		#CopyLauncher
		tfolder = bpy.utils.user_resource('DATAFILES') + LIBNAME + os.sep + 'launcher' + os.sep
		ext = ".exe" if my_platform.startswith("WIN") else ""
		launcher_path = tfolder + my_platform + ext
		shutil.copyfile(launcher_path, out + game_name + ext)
		shutil.copyfile(tfolder + "config.txt", out + "config.txt")
		#TODO, Make launcher build and make them export PYTHONPATH for components
		#TODO, Enable icon select on windows
		
		#Copy BlenderPlayer
		version_major, version_minor, _ = bpy.app.version
		blender_path = os.path.abspath('.') + os.sep if utils.getPlatformCode() == my_platform \
			else bpy.utils.user_resource('DATAFILES') + LIBNAME + os.sep + 'platform' + os.sep + utils.getPlatformCode() + os.sep
		python_path = str(version_major) + "." + str(version_minor) + os.sep + "python" + os.sep + "lib" + os.sep
				
		if not os.path.isdir(blender_path) or not os.path.isfile(blender_path + "blenderplayer" + ext) or not os.path.isdir(blender_path + python_path):
			self.report({'ERROR'}, "BlenderPlayer not found!")
			#TODO: NetInstall Options (but manual, not here)
			return {'CANCELLED'}
			
		try:
			print(out + "engine" + os.sep + python_path)
			utils.copytree(blender_path + python_path, out + "engine" + os.sep + python_path, callback=prog)
		except TimeoutError:
			self.report({'ERROR'}, "Timeout!")
			#return {'CANCELLED'}
			
		if my_platform.startswith("WIN"): #Copy DLL
			for x in os.listdir(blender_path):
				if x.endswith(".dll"): shutil.copyfile(blender_path + x, out + "engine" + os.sep + x)
				
		shutil.copyfile(blender_path + "blenderplayer" + ext, out + "engine" + os.sep + "blenderplayer" + ext)
		
		return {'FINISHED'}


	def invoke(self, context, event):
		wm = context.window_manager
		return wm.invoke_props_dialog(self, width=600)

	def draw(self, context):
		layout = self.layout
		box = layout.box()
		col = box.column()
		col.label("Choose operating system you want to export to: ")
		rowsub = col.row()
		rowsub.prop(self, "platform")
	
		box = layout.box()
		col = box.column()
		rowsub = col.row()
		rowsub.prop(self, "output_path")
		
		


def register():
	bpy.utils.register_class(ExportGameProject)
 
def unregister():
	bpy.utils.unregister_class(ExportGameProject)