import bge, mathutils
from collections import OrderedDict

#If false, we don't have blender avaliable.
with_bpy = False
try:
	import bpy
	with_bpy = True
except Exception: pass
	
class Music(bge.types.KX_PythonComponent):
	""" Play a long audio file
	
	.. attribute:: File
	
		The filepath to to the file to play. Relative to the project folder. (Python: path, audiofile)
		
	.. attribute:: Volume, Loop
	
	.. attribute:: Fade In
	
		The amount of time in seconds for the fade in effect. (Python: fade)
		
	
	"""

	args = OrderedDict([
		("File", "test.mp4"),
		("Volume", 1.000),
		("Fade In", 2.0),
		("Loop", False),
	])

	def start(self, args):
		self.audiofile = None
		self.path = args['File']
		self.volume = args["Volume"]
		self.loop = args["Loop"]
		self.fade = args["Fade"]

	def update(self):
		if self.audiofile == None:
			from core import media
			self.audiofile = media.AudioFile(self.path).play(loop=self.loop, volume=self.volume, transition=(self.fade, 2, 3))
			
class MusicFolder(bge.types.KX_PythonComponent):
	""" Continuously play random music from a folder
	
	.. attribute:: Folder
	
		The filepath to to the folder to play. Relative to the project folder. (Python: path, audiofile)
		
	.. attribute:: Volume
	
	.. attribute:: Fade
	
		The amount of time in seconds for the (fade out -> wait -> fade in) effect during song transitions. (Python: fade)
		
		:type: set(3)
	
	"""

	args = OrderedDict([
		("Folder", "media/music"),
		("Volume", 1.000),
		("Fade", (5.0, 2.0, 4.0)),
	])

	def start(self, args):
		self.audiofile = None
		self.path = args['Folder']
		self.volume = args["Volume"]
		self.fade = args["Fade"]

	def update(self):
		if self.audiofile == None:
			from core import media
			
			self.audiofile = media.AudioFile()
			self.audiofile.volume_max = self.volume
			media.RandomMusic(audiofile=self.audiofile).play(self.path)
			
			
class Video(bge.types.KX_PythonComponent):
	""" Play a video file with sound
	
	.. attribute:: File
	
		The filepath to to the file to play. Relative to the project folder. (Python: path, videofile)
		
	.. attribute:: Volume
	
	"""

	args = OrderedDict([
		("File", "test.mp4"),
		("Volume", 1.000),
	])

	def start(self, args):
		self.videofile = None
		self.path = args['File']
		self.volume = args["Volume"]

	def update(self):
		if self.videofile == None:
			from core import media
			
			self.videofile = media.Screen(self.object)
			self.videofile.play(self.path)
			speaker = self.videofile.speaker
			if speaker: speaker.volume = self.volume
			
		
	