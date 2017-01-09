from bge import logic, texture
from core import module, utils, sequencer
import aud
import os.path

#===================================
#			SREEN CLASS
#===================================
class Screen():
	""" The base object used in this widget will become a screen.
	
	:param object: Object to apply the changes.
	:type object: |KX_GameObject| or string
	
	.. attribute:: obj
	
		The |KX_GameObject| used as screen.
	
	.. attribute:: speaker
	
		The AudioFile of the video if used, otherwise None.
	
	.. attribute:: frame
	
		The number of the frame being played.
	
	.. attribute:: callback
	
		A function to call once the reproduction ends. Will be overwrited with the paramater specified on the ``play`` method, even if it's ``None``.
	"""
	
	def __init__(self, obj=None):
		self.obj = obj
		self.callback = None
		self.true_start_file = None
		self.frame = 0
		self.speaker = None
		
		if obj == None:
			logic.LibLoad(logic.expandPath("//core/misc/screen.blend"), 'Scene')
			obj = self.obj = logic.getCurrentScene().objects["__CORE__Screen"]
			obj.visible = False
		
		try:
			t = obj.meshes[0].materials[0].textures[0]
			if t == None: raise Exception
		except Exception:
			try:
				logic.LibLoad(logic.expandPath("//core/misc/screen.blend"), 'Mesh')
				obj.replaceMesh("__CORE__Screen")
			except Exception:
				utils.debug("Video not set, " + obj.name + " object is not a screen. Make sure it has a texture to an image file. ")
				self.play = self.no_play
				self.replaceTexture = self.no_replaceTexture
				
			
	def no_play(self, x, callback=None): return
	
	def no_replaceTexture(self, filepath): return
	def replaceTexture(self, filepath):
		""" Change the texture of the object by another, external, texture.
		
		:param string filepath: The relative path (from the data folder) of the texture/image to replace.		
		"""
		if filepath == None:
			try: del self.texture
			except: pass
			try: del self.video.source
			except: pass
			try: del self.video
			except: pass
			return
		
		path = logic.expandPath("//" + filepath)
		self.texture = texture.Texture(self.obj, 0)
		self.texture.source = texture.ImageFFmpeg(path)
		self.texture.refresh(False)
		
	def no_play(self, x, callback=None): return
	def play(self, video, callback=None):
		""" Plays a video on this screen, also makes the *speaker* aviable.
		
		:param string video: The relative path (from the data folder) of the video to use.
		:param function callback: Function to call once the video ends.
		"""
		#Video
		path = logic.expandPath("//" + video)
		if not os.path.isfile(path): raise FileNotFoundError(path + " doesn't exist")
		self.video = texture.Texture(self.obj, 0)
		self.video.source = texture.VideoFFmpeg(path)
		self.video.source.scale = True
		self.video.source.play()
		module.video_playback_list.append(self)
		
		#Audio
		try:
			self.speaker = AudioFile()
			self.speaker = self.speaker.play(video)
		except RuntimeError: pass
			
		#Callback
		self.callback = callback
		
		return self
		
	def fadeIn(self, time):
		"""Starts to make fadein now. It actuates over the alpha chanel of the |KX_GameObject| representing this screen. In order to work it needs *object color* enabled on the material.
		
		:param float time: How long the fadein lasts.
		"""
		sequencer.LinearInterpolation(self.obj.color.w, 1, time, self._interpol)
	
	def fadeOut(self, time):
		"""Starts to make fadeout now. It actuates over the alpha chanel of the |KX_GameObject| representing this screen. In order to work it needs *object color* enabled on the material.
		
		:param float time: How long the fadein lasts.
		"""
		sequencer.LinearInterpolation(self.obj.color.w, 0, time, self._interpol)
	
	def _interpol(self, x):
		self.obj.color.w = x
		
	def updateVideo(self):
		self.video.refresh(True)
		if self.video.source.status == 2:
			self.frame += 1
			
		if self.video.source.status == 3:
			self.frame = 0
			module.video_playback_list.remove(self)
			if self.callback: self.callback()
		
			
#===============================================
#						AUDIO
#===============================================

device = aud.device()

class AudioFile():
	""" A object representating an audio file. Initializating this won't play the file.
	
	* Recomended formats: **.mp3**
	* Supported Formats: **.mp3**, **.ogg**, **.wav**
	
	.. note:: This is done in a new thread, changing scenes or a low framerate won't alter the sound.
	
	:param string filepath: Relative path (from the data folder) of the audio file to use.
	:param function callback: Function to call once the playback ends.
	
	.. attribute:: handle
	
		The *aud.Handle*, be coutious while tweaking with this.
		
	.. attribute:: volume_min
	
		Minium volume of the audio.
		
	.. attribute:: volume_max
	
		Maxium volume of the audio.
	
	.. attribute:: time
	
		The amount of time in seconds since the file start playing.
	
	"""
	def __init__(self, filepath = "", callback = None):
		self.filepath = filepath
		self.rcall = callback
		self.time = 0
		self.handle = None
		self.volume_min = 0
		self.volume_max = 1
		self.callback = None
		self._volume = 1

		#LinearInterpolation Objects
		self.fadein = None
		self.fadeout = None
		
		#Status
		self.playing = False
		self.waiting = False
	
	def _transition_callback(self, n):
		self.volume = 0
		self.playing = False
		self.waiting = False
		self.play(callback=self.callback)
		self.fadeIn(n)
	
	def play(self, filepath=None, loop=False, volume = None, pitch = 1, callback = None, transition = (3, 2, 3)):
		""" Method to play an audio file.
		
		If an audio file is being played while calling this, it will be replaced by a new one. During the transation a *fadeOut->FadeIn* effect will occur.
		
		:param string filepath: Relative path (from the data folder) of the audio file to use.
		:param bool loop: If true the audio will be played in loop.
		:param float volume: The volume of the audio file relative to the master device. (Default = 1.0)
		:param float pitch: The pitch.
		:param function callback: Function to call once the playback ends.
		:param tuple transition: The times for the fade effect during transations. In order: Duration of the fadeout, time for the fadein to start, duration of the fadein. In sconds.
		"""
		
		if self.waiting == True: #Replace sound that will be played.
			self.filepath = filepath
			return
			
		x, y, z = transition
		if self.playing == True: #FadeOut this sound and fadeIn the new one.
			dummy = self.moveInstance()
			dummy.fadeOut(x, stop=True)

			if filepath: self.filepath = filepath
			self.waiting = True
			
			sequencer.Wait(y, lambda: self._transition_callback(z))
			self.callback = callback
			return
		elif x > 0:
			x, y, z = transition
			copy_volume_max = self.volume_max
			self.volume_max = volume if volume != None else self.volume_max
			self.volume = 0
			self.fadeIn(x)
			self.volume_max = copy_volume_max
		
		self.callback = callback
		if not filepath: filepath = self.filepath
		else: self.filepath = filepath
		path = logic.expandPath("//" + filepath)
		factory = aud.Factory(path)
		
		try:
			self.factory = factory
			self.handle = device.play(self.factory) #It sends a callback that will play the music on a new theread.
			self.handle.pitch = pitch
			if volume == None: self.volume = self._volume
			else: self.volume = volume
			if loop: self.handle.loop_count = -1
		except:
			if os.path.isfile(path) == False: raise FileNotFoundError(path)
			else: raise RuntimeError("AudioFile Load Error: " + path)
		
		self.playing = True
		module.low_frequency_callbacks.append(self.update)
		return self
		
	def fadeOut(self, time, stop = False):
		"""Starts to make fadeout now.
		
		:param float time: How long the fadeout lasts.
		:param bool stop: If True it will automatically stop the reproduction at the end.
		"""
		if self.fadeout and self.fadeout.status != False:
			self.fadeout.delete()
		
		if self.fadein and self.fadein.status != False:
			self.fadein.delete()
			
		if stop:
			self.fadeout = sequencer.LinearInterpolation(self.volume, self.volume_min, time, self._interpol, self.stop)
		else:
			self.fadeout = sequencer.LinearInterpolation(self.volume, self.volume_min, time, self._interpol)
		
	def fadeIn(self, time):
		"""Starts to make fadein now.
		
		:param float time: How long the fadein lasts.
		"""
		if self.fadein and self.fadein.status != False:
			self.fadein.delete()
		
		if self.fadeout and self.fadeout.status != False:
			self.fadeout.delete()
			
		self.fadein = sequencer.LinearInterpolation(self.volume, self.volume_max, time, self._interpol)
	
	def _interpol(self, x):
		self.volume = x
		
	def moveInstance(self):
		""" Returns a new instance of this class and gives it control over the audiofile, this instance returns to its original state.
		
		.. Note:: This function is used internally to replace sounds with a fadeIn/fadeOut effect were they can be mixed during the transition.
		"""
	
		dummy = AudioFile()
		dummy.__dict__ = self.__dict__.copy()
		self.handle = None
		self.factory = None
		self.time = 0
		self.playing = False
		self.waiting = False
		module.low_frequency_callbacks.remove(self.update)
		module.low_frequency_callbacks.append(dummy.update)
		return dummy
	
	def resume(self):
		self.handle.play()
		self.playing = True
	
	def pause(self):
		pass
	
	def stop(self):
		""" Stops the sound. """
		
		module.low_frequency_callbacks.remove(self.update)
		self.playing = False
		self.handle.stop()
		self.time = 0
		if self.callback: self.callback()
		elif self.rcall:  self.rcall()
	
	@property
	def volume(self):
		""" """
		try: return self.handle.volume
		except: return self._volume
		
	@volume.setter
	def volume(self, x):
		try:
			if x < self.volume_min: self.handle.volume = self.volume_min
			elif x > self.volume_max: self.handle.volume = self.volume_max
			else: self.handle.volume = x
		except: self._volume = x
	
	def update(self, time):
		if self.handle and self.handle.status == False:
			self.stop()
		else:
			self.time += time
		
music = AudioFile("")
sui = {}

class AudioEffect:
	""" It buffers a sound file in memory for faster usage.
	
	:param string filepath: The relative path to the sound file.
	"""

	def __init__(self, filepath):
		path = logic.expandPath("//" + filepath)
		factory = aud.Factory(path)
		self.factory = factory.buffer()
		self.handle = None
		
	def play(self, volume = 1, pitch = 1):
		""" Plays the sound """
		self.handle = device.play(self.factory)
		self.handle.volume = volume
		self.handle.pitch = pitch
		
class RandomMusic:
	""" Plays random music from a directory.
	
	To use it correctly initialize it somewere and call ``play()`` when you want to start playing music or you want to go to the next song.
	
	:param string directory: The path of the directory.
	:param bool loop: If true it continues playing new songs until ``stop()`` is called.
	:param AudioFile audiofile: The AudioFile object to use. By the default ``media.music``.
	:param transition: The times for the fade effect when changing songs.
	
	.. attribute:: playing
	
		No songs will be played if it is not True.
		:type: bool
		
	.. attribute:: ignore
	
		List of filenames to ignore.

	"""
	
	def __init__(self, directory = "media/music", loop = True, audiofile = music, transition = (5, 2, 4)):
		self.loop = loop
		if not directory.endswith('/'): directory += '/'
		self.directory = directory
		self.transition = transition
		self.ignore = []
		
		self.playing = False
		self.audiofile = audiofile
		if loop: module.low_frequency_callbacks.append(self.update)
		
	def play(self, directory = None):
		""" Plays a song, or replaces the current song. """
		if directory:
			if not directory.endswith('/'): directory += '/'
			self.directory = directory
		if self.audiofile.waiting == False:
			self.next()
			self.playing = True
		
	def stop(self):
		""" Stops playing songs and stops the current song """
		if self.playing:
			try:
				module.low_frequency_callbacks.remove(self.update)
				self.audiofile.fadeOut(self.transition[2], True)
				self.playing = False
			except IndexError:
				pass
		
	def next(self):
		""" Plays a song, or replaces the current song. """
		current_song = self.audiofile.filepath
		path = self.getRandomFileTrack()
		try:
			self.audiofile.play(self.directory + path, transition = self.transition)
		except IndexError: utils.debug("No music found in directory " + self.directory)
		except RuntimeError as e:
			utils.debug(e)
			self.ignore.append(path)
			self.audiofile.filepath = current_song
			self.next()
			
		
	def getRandomFileTrack(self):
		""" Returns a random filename with any extension. """
		current_song = os.path.basename(self.audiofile.filepath)
		path = logic.expandPath("//" + self.directory)
		files = [x for x in os.listdir(path) if current_song != x and not x in self.ignore]
		if files: return utils.choice(files)
		else: return current_song
		
	def update(self, time):
		if self.audiofile.playing == False and self.playing == True:
			self.play()
			
			