
class Screen:
	"""The base object used in this widget will become a screen."""

	def __init__(self, obj=None):
		self.obj = None
		self.speaker = None
		self.frame = None
		self.callback = None

	def replaceTexture(self, filepath):
		"""Change the texture of the object by another, external, texture."""

	def play(self, video, callback=None):
		"""Plays a video on this screen, also makes the speaker aviable."""

	def fadeIn(self, time):
		"""Starts to make fadein now. It actuates over the alpha chanel of the KX_GameObject representing this screen. In order to work it needs object color enabled on the material."""

	def fadeOut(self, time):
		"""Starts to make fadeout now. It actuates over the alpha chanel of the KX_GameObject representing this screen. In order to work it needs object color enabled on the material."""

device = None
music = None

class AudioFile:
	"""A object representating an audio file. Initializating this won’t play the file."""

	def __init__(self, filepath='', callback=None):
		self.handle = None
		self.volume_min = None
		self.volume_max = None
		self.time = None
		self.volume = None

	def play(self, filepath=None, loop=False, volume=None, pitch=1, callback=None, transition=(3, 2, 3)):
		"""Method to play an audio file."""

	def fadeOut(self, time, stop=False):
		"""Starts to make fadeout now."""

	def fadeIn(self, time):
		"""Starts to make fadein now."""

	def moveInstance(self):
		"""Returns a new instance of this class and gives it control over the audiofile, this instance returns to its original state."""

	def stop(self):
		"""Stops the sound."""


class RandomMusic:
	"""Plays random music from a directory."""

	def __init__(self, directory='media/music', loop=True, audiofile=None, transition=(5,0,0)):
		self.playing = None
		self.ignore = None

	def play(self, directory=None):
		"""Plays a song, or replaces the current song."""

	def stop(self):
		"""Stops playing songs and stops the current song"""

	def next(self):
		"""Plays a song, or replaces the current song."""

	def getRandomFileTrack(self):
		"""Returns a random filename with any extension."""

