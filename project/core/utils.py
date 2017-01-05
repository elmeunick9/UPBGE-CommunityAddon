from bge import logic, types
from mathutils import Vector, geometry
from random import randint, choice, seed
import time
from time import sleep
import bisect
import os

seed(time.time())

try:
	from script import constant
except Exception:
	constant = None
		
def loadGameProperty(name):
	""" Loads a property from your :file:`config.txt` file.

		The property is loaded as string, then you use the type name to get the apropiate type.
		*e.j:* ``media.device.volume = float(utils.loadGameProperty("volume"))``

		Raises ``KeyError`` if the property is not found.

		:param string name: Name of the property to load.
		:return: A string containing the value of the property.
	"""
	path = getLocalDirectory() + "config.txt"
	with open(path, "r") as input:
		for l in input.read().splitlines():
			if len(l) == 0: continue
			if l[0] == '#': continue

			x = l.find(name)
			y = l.find(": ")
			if x == 0 and y > 0:
				prop = l[y+2:]
				return prop

	raise KeyError("Property " + name + " not found in the configuration file. ")

def saveGameProperty(name, value):
	""" Saves a property to your :file:`config.txt` file.

	:param string name: Name of the property to load.
	:param value: Value to save, will be converted into a string.
	"""
	path = getLocalDirectory() + "config.txt"
	with open(path, "r+") as input:
		match = False
		new = ""
		for l in input.read().splitlines():
			if len(l) == 0 or l[0] == '#':
				new += l + '\n'
				continue

			x = l.find(name)
			y = l.find(": ")
			if x == 0 and y > 0 and not match:
				l = l[:y+2]
				l += str(value)
				match = True
			new += l + '\n'

		if not match:
			new += "\n" + name + ": " + str(value)
		input.seek(0)
		input.write(new)
		
def getBlendFilepath():
	""" Returns the blend file absolute filepath, including the name. """
	try:
		from bpy import data
		return data.filepath
	except ImportError:
		import sys
		path = [x for x in sys.argv if x.endswith(".blend") or x.endswith(".blend~")][0]
		if path[-1] == '~': path = path[:-1]
		return logic.expandPath("//" + os.path.basename(path))
		

_local_data_directory = None
def getLocalDirectory():
	""" Returns the directory where local data can be stored. By default the same directory than the game. If there is no write acces then a directory inside the user folder. """
	global _local_data_directory
	if _local_data_directory == None:
		game_name = os.path.normpath(logic.expandPath('//..//'))
		game_name = game_name[game_name.rfind(os.sep)+len(os.sep):]
		try:
			path = logic.expandPath("//../")
			f = open(path + "config.txt", 'a')
			_local_data_directory = path
		except PermissionError:
			from sys import platform as _platform
			if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
				path = os.getenv("HOME") + "/.local/share/" + game_name + '/'
			elif _platform == "win32" or _platform == "cygwin":
				import ctypes.wintypes
				CSIDL_PERSONAL = 5       # My Documents
				SHGFP_TYPE_CURRENT = 0   # Get current, not default value

				buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
				ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
				path = buf.value + os.sep + "My Games" + os.sep

			_local_data_directory = path + game_name + os.sep

		else: f.close()

	if os.path.isdir(_local_data_directory):
		return _local_data_directory
	else:
		path = _local_data_directory
		os.makedirs(path)
		import shutil
		shutil.copyfile(logic.expandPath("//../config.txt"), path + "config.txt")
		return path

def debug(text):
	""" Prints *text* if ``CORE_DEBUG_PRINT`` is enabled. """
	if constant:
		if constant.CORE_DEBUG_PRINT == True: print(text)
	else: print(text)

def verbose(text):
	""" Prints *text* if ``CORE_DEBUG_VERBOSE`` is enabled. """
	if constant:
		if constant.CORE_DEBUG_VERBOSE == True: print(text)
	else: print(text)

def randRGB(r = None, g = None, b = None, a = 1):
	""" Generates a random vector representing a color, paramaters not *None* will use that value instead of generating a new one. """
	if not r: r = randint(0,100)/100
	if not g: g = randint(0,100)/100
	if not b: b = randint(0,100)/100
	if not a: a = randint(0,100)/100
	return Vector((r,g,b,a))
	
def getTimeFromString(text):
	""" Returns a float reperesenting time in seconds from a string formatted like: hh:mm:ss,sss"""
	text = text.replace(',', '.')
	hours, minutes, seconds = (0, 0, 0)
	l = text.split(':')
	if len(l) == 1: seconds = float(l)
	if len(l) == 2: minutes, seconds = int(l[0]), float(l[1])
	if len(l) == 3: hours, minutes, seconds = int(l[0]), int(l[1]), float(l[2])
	return hours*3600 + minutes*60 + seconds

def getNearestVertexToPoly(object, poly, point):
	""" Returns the nearest vertext to a poligon.

	:param poly: The poligon if wich vertex you want to check.
	:type poly: |KX_PolyProxy|
	:param point: The point to check, in world coordinates.
	:type point: |Vector|
	"""

	if not type(point) is Vector: point = Vector(point)
	mesh = poly.getMesh()

	min = None
	f = None
	for i in range(poly.getNumVertex()):
		v = mesh.getVertex(0, poly.getVertexIndex(i))
		r = vectorFrom2Points(v.XYZ, point - object.worldPosition).length
		if not min or r < min:
			min = r
			f = v

	return f
	
def getNearestObject(obj, property="", max_distance=0):
	""" Returns the closest object to 'obj'. If there isn't any, returns itself.
	
	:param obj: The base object
	:type poly: |KX_GameObject|
	:param property: If any, will filter only objects with this property. If it's a Bool must be checked as True
	:type property: string
	:param max_distance: Filter objects within this distance. If 0, do not filter distance.
	:type property: float
	"""

	if property == "":	obj_list = [x for x in obj.scene.objects if x != obj and obj.getDistanceTo(x) <= max_distance] 
	else: 				obj_list = [x for x in obj.scene.objects if x.get(property, False) != False and x != obj and obj.getDistanceTo(x) <= max_distance]
	
	if len(obj_list) == 0: return obj
	
	closest  = obj_list[0]
	distance = obj.getDistanceTo(closest)

	for object in obj_list[1:]:
		new_distance = obj.getDistanceTo(object)
		if new_distance < distance:
			closest = object
			distance = new_distance
			
	return(closest)

def getPolyNormal(poly):
	""" Returns the normal of poligon based on the position of their vertex. It calculates the normal, it doesn't return manually modified normals.

	:param poly: The poligon.
	:type poly: |KX_PolyProxy|
	"""

	mesh = poly.getMesh()
	s = poly.getNumVertex()
	v1 = mesh.getVertex(0, poly.v1)
	v2 = mesh.getVertex(0, poly.v2)
	v3 = mesh.getVertex(0, poly.v3)
	if s == 4: v4v = mesh.getVertex(0, poly.v4).XYZ
	else: v4v = None

	if v4v: normal = geometry.normal(v1.XYZ, v2.XYZ, v3.XYZ, v4v)
	else: normal = geometry.normal(v1.XYZ, v2.XYZ, v3.XYZ)
	return normal

def recalculateNormals(obj):
	""" Recalculates the normals of a |KX_GameObject|, |KX_MeshProxy| or |KX_PolyProxy|.

	It iterates through all the given vertex, it may be a slow operation, use with caution. """

	if type(obj) is types.KX_GameObject:
		mesh = obj.meshes[0]
	elif type(obj) is types.KX_MeshProxy: mesh = obj
	elif type(obj) is types.KX_PolyProxy: mesh = obj.getMesh()
	else: raise ValueError("Argument must be KX_GameObject, KX_MeshPoxy or KX_PolyProxy, not " + str(type(obj)))
	verdict = {} #Vertex Dictionary LOL

	#Iterate throught Faces and make a list with all the vertex and the normals of the faces the are part of.
	if type(obj) is not types.KX_PolyProxy:
		for i in range(mesh.numPolygons):
			poly = mesh.getPolygon(i)
			normal = getPolyNormal(poly)

			for j in range(poly.getNumVertex()):
				try:
					verdict[poly.getVertexIndex(j)].append(normal)
				except KeyError:
					verdict[poly.getVertexIndex(j)] = [normal]
	else:
		poly = obj
		normal = getPolyNormal(poly)

		for j in range(poly.getNumVertex()):
			try:
				verdict[poly.getVertexIndex(j)].append(normal)
			except KeyError:
				verdict[poly.getVertexIndex(j)] = [normal]

	#Iterate throught the list recalculating the normal of each vertex.
	for i, normals in verdict.items():
		normal = Vector([0,0,0])
		for n in normals:
			normal += n
		s = len(normals)
		if s == 0: continue
		normal.x /= s
		normal.y /= s
		normal.z /= s
		normal.normalize()
		mesh.getVertex(0, i).setNormal(normals[0].to_tuple())

def rand10():
	""" Generates a rondom integer from 0 to 9 """
	return randint(0,9)

def vectorFrom2Points(origin, dest, module = None):
	""" Returns a |Vector|  form 2 points in the space.

	:param origin: Point A
	:type origin: |Vector|
	:param dest: Point B
	:type dest: |Vector|
	:param float module: If setted, the returned vector will have this maxium lenght. The new lenght will never be greater than the original.
	"""
	vec = Vector((dest.x - origin.x, dest.y - origin.y, dest.z - origin.z))
	if not module: return vec

	l = vec.length

	if l < 0.0125: return vec.zero()
	if l < module: return vec

	vec = vec / l
	if module == 1: return vec
	else: return vec * module

def moveObjectToObject(origin, dest, speed = 1):
	""" Moves *origin* to *dest* at a speed of *speed*. Must by called every frame for a complete movement.

	:param origin: Object to move.
	:type origin: |KX_GameObject|
	:param dest: Destination object.
	:type dest: |KX_GameObject|
	:param float speed: The amount of movment to do in one frame.
	:return: True if the object has been moved, false otherwise.
	"""
	return moveObjectToPosition(origin, dest.position, speed)

def moveObjectToPosition(origin, dest, speed = 1):
	""" Moves *origin* to *dest* at a speed of *speed*. Must by called every frame for a complete movement.

	:param origin: Object to move.
	:type origin: |KX_GameObject|
	:param dest: Destination object.
	:type dest: |Vector|
	:param float speed: The amount of movment to do in one frame.
	:return: True if the object has been moved, false otherwise.
	"""
	fr = logic.getAverageFrameRate()
	if fr < 20: fr = 20
	vel = speed / fr
	vec = vectorFrom2Points(origin.position, dest, vel)
	if vec:
		origin.position += vec
		return True
	else: return False

def removeAll(original_list, sublist):
	""" Removes all ocurrences of any of the values of sublist from original_list"""
	l = []
	for x in original_list:
		inl = False
		for y in sublist:
			if x == y: inl = True
		if not inl and x not in l: l.append(x)

	return l

#Scene Managment
def getSceneByName(name):
	""" Get a scene by its name. Only works with loaded scenes.

	.. deprecated:: 0.3
		Use ``module.scene_game`` or ``module.scene_gui`` instead.

	"""
	for scn in logic.getSceneList():
		if scn.name == name: return scn

#GLSL 2DFilters
import core.glsl as filter2D

