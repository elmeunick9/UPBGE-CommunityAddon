
def getBlendFilepath():
	"""Returns the blend file absolute filepath, including the name."""

def getLocalDirectory():
	"""Returns the directory where local data can be stored. By default the same directory than the game. If there is no write acces then a directory inside the user folder."""

def loadGameProperty(name):
	"""Loads a property from your config.txt file."""

def saveGameProperty(name, value):
	"""Saves a property to your config.txt file."""

def debug(text):
	"""Prints text if CORE_DEBUG_PRINT is enabled."""

def verbose(text):
	"""Prints text if CORE_DEBUG_VERBOSE is enabled."""

def rand10():
	"""Generates a rondom integer from 0 to 9"""

def randRGB(r=None, g=None, b=None, a=1):
	"""Generates a random vector representing a color, paramaters not None will use that value instead of generating a new one."""

def getNearestObject(obj, property='', max_distance=0):
	"""Returns the closest object to ‘obj’. If there isn’t any, returns itself."""

def getNearestVertexToPoly(object, poly, point):
	"""Returns the nearest vertext to a poligon."""

def getPolyNormal(poly):
	"""Returns the normal of poligon based on the position of their vertex. It calculates the normal, it doesn’t return manually modified normals."""

def recalculateNormals(obj):
	"""Recalculates the normals of a KX_GameObject, KX_MeshProxy or KX_PolyProxy."""

def vectorFrom2Points(origin, dest, module=None):
	"""Returns a mathutils.Vector  form 2 points in the space."""

def moveObjectToObject(origin, dest, speed=1):
	"""Moves origin to dest at a speed of speed. Must by called every frame for a complete movement."""

def moveObjectToPosition(origin, dest, speed=1):
	"""Moves origin to dest at a speed of speed. Must by called every frame for a complete movement."""

def removeAll(original_list, sublist):
	"""Removes all ocurrences of any of the values of sublist from original_list"""
