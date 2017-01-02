from .macro import *

import bpy
import os, shutil, zipfile

def check():
	base = bpy.utils.user_resource('DATAFILES') + LIBNAME + os.sep
	verfile = base + "addon_info.txt"
	
	if os.path.isfile(verfile):
		file = open(verfile, "r")
		file_version = file.read()
		if file_version != str(VERSION):
			print(LIBNAME + " #001: Versions don't match, I'll proced to reinstall myself.")
			new_install(verfile)
		if not os.path.exists(base + "launcher"):
			print(LIBNAME + " #002: Launcher broken, I'll proced to reinstall myself.")
			new_install(verfile)
	   
	else: new_install(verfile)
		
def new_install(version_filepath): #Of the addon, not blender
	#Delete old data
	platform_folder = os.path.dirname(version_filepath)
	try:
		shutil.rmtree(platform_folder)
	except: pass
	
	#Update the version file
	if not os.path.exists(platform_folder):
		os.makedirs(platform_folder)
	
	file = open(version_filepath, "w")
	file.write(str(VERSION))
	file.close()

	#Install data.zip
	try:
		addon_folder = bpy.utils.user_resource('SCRIPTS', 'addons' + os.sep + LIBNAME + os.sep)
		filepath = addon_folder + 'data.zip'
		
		zip = zipfile.ZipFile(filepath)
		zip.extractall(platform_folder)
		zip.close()

	except Exception as ex:
		print(ex)
		return

	#Greets the user
	print(LIBNAME + ": Hello, I've been installed!")
	#print("Check how to use me on my thread --> http://blenderartists.org/forum/showthread.php?340504-Build-Game-Addon")
	
def uninstall():
	base = bpy.utils.user_resource('DATAFILES') + LIBNAME + os.sep
	shutil.rmtree(base)
