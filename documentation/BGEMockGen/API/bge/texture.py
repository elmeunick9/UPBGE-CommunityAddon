
class VideoFFmpeg:
	"""FFmpeg video source."""

	def __init__(self, file=None, capture=-1, rate=25.0, width=0, height=0):
		self.status = int()
		self.range = [0.0,0.0]
		self.repeat = int()
		self.framerate = float()
		self.valid = bool()
		self.image = None
		self.size = (0,0)
		self.scale = bool()
		self.flip = bool()
		self.filter = None
		self.preseek = int()
		self.deinterlace = bool()

	def play(self):
		"""Play (restart) video."""
		return bool()

	def pause(self):
		"""Pause video."""
		return bool()

	def stop(self):
		"""Stop video (play will replay it from start)."""
		return bool()

	def refresh(self, buffer=None, format="RGBA", timestamp=-1.0):
		"""Refresh video - get its status and optionally copy the frame to an external buffer."""
		return int()


class ImageFFmpeg:
	"""FFmpeg image source."""

	def __init__(self, file=None):
		self.status = int()
		self.valid = bool()
		self.image = None
		self.size = (0,0)
		self.scale = bool()
		self.flip = bool()
		self.filter = None

	def refresh(self, buffer=None, format="RGBA"):
		"""Refresh image, get its status and optionally copy the frame to an external buffer."""
		return int()

	def reload(self, newname=None):
		"""Reload image, i.e. reopen it."""


class ImageBuff:
	"""Image source from image buffer."""

	def __init__(self, width=None, height=None, color=0, scale=False):
		self.filter = None
		self.flip = bool()
		self.image = None
		self.scale = bool()
		self.size = (0,0)
		self.valid = bool()

	def load(self, imageBuffer, width, height):
		"""Load image from buffer."""

	def plot(self, imageBuffer, width, height, positionX, positionY, mode=None):
		"""Update image buffer."""


class ImageMirror:
	"""Image source from mirror."""

	def __init__(self, scene=None, observer=None, mirror=None, material=0, width=None, height=None, samples=None, hdr=None):
		self.alpha = bool()
		self.horizon = float()
		self.zenith = float()
		self.background = float()
		self.updateShadow = bool()
		self.colorBindCode = int()
		self.capsize = [0,0]
		self.clip = float()
		self.filter = None
		self.flip = bool()
		self.image = None
		self.scale = bool()
		self.size = (0,0)
		self.valid = bool()
		self.whole = bool()

	def refresh(self, buffer=None, format="RGBA"):
		"""Refresh image - render and copy the image to an external buffer (optional)
then invalidate its current content."""


class ImageMix:
	"""Image mixer."""

	def __init__(self):
		self.filter = None
		self.flip = bool()
		self.image = None
		self.scale = bool()
		self.size = (0,0)
		self.valid = bool()

	def getSource(self, id):
		"""Get image source."""
		return VideoFFmpeg()

	def getWeight(self, id):
		"""Get image source weight."""
		return int()

	def refresh(self, buffer=None, format="RGBA"):
		"""Refresh image - calculate and copy the image to an external buffer (optional)
then invalidate its current content."""

	def setSource(self, id, image):
		"""Set image source - all sources must have the same size."""

	def setWeight(self, id, weight):
		"""Set image source weight - the sum of the weights should be 256 to get full color intensity in the output."""


class ImageRender:
	"""Image source from render.
The render is done on a custom framebuffer object if fbo is specified,
otherwise on the default framebuffer."""

	def __init__(self, scene=None, camera=None, width=None, height=None, samples=None, hdr=None):
		self.alpha = bool()
		self.horizon = float()
		self.zenith = float()
		self.background = float()
		self.updateShadow = bool()
		self.colorBindCode = int()
		self.capsize = [0,0]
		self.filter = None
		self.flip = bool()
		self.image = None
		self.scale = bool()
		self.size = (0,0)
		self.valid = bool()
		self.whole = bool()
		self.depth = bool()
		self.zbuff = bool()

	def render(self):
		"""Render the scene but do not extract the pixels yet.
The function returns as soon as the render commands have been send to the GPU.
The render will proceed asynchronously in the GPU while the host can perform other tasks.
To complete the render, you can either call refresh()
directly of refresh the texture of which this object is the source.
This method is useful to implement asynchronous render for optimal performance: call render()
on frame n and refresh() on frame n+1 to give as much as time as possible to the GPU
to render the frame while the game engine can perform other tasks."""
		return bool()

	def refresh(self): pass

	def refresh(self, buffer, format="RGBA"):
		"""Refresh video - render and optionally copy the image to an external buffer then invalidate its current content.
The render may have been started earlier with the render() method,
in which case this function simply waits for the render operations to complete.
When called without argument, the pixels are not extracted but the render is guaranteed
to be completed when the function returns.
This only makes sense with offscreen render on texture target (see offScreenCreate())."""
		return bool()


class ImageViewport:
	"""Image source from viewport."""

	def __init__(self):
		self.alpha = bool()
		self.capsize = [0,0]
		self.filter = None
		self.flip = bool()
		self.image = None
		self.position = [0,0]
		self.scale = bool()
		self.size = (0,0)
		self.valid = bool()
		self.whole = bool()
		self.depth = bool()
		self.zbuff = bool()

	def refresh(self, buffer=None, format="RGBA"):
		"""Refresh video - copy the viewport to an external buffer (optional) then invalidate its current content."""


class VideoDeckLink:
	"""Image source from an external video stream captured with a DeckLink video card from
Black Magic Design.
Before this source can be used, a DeckLink hardware device must be installed, it can be a PCIe card
or a USB device, and the ‘Desktop Video’ software package (version 10.4 or above must be installed)
on the host as described in the DeckLink documentation.
If in addition you have a recent nVideo Quadro card, you can benefit from the ‘GPUDirect’ technology
to push the captured video frame very efficiently to the GPU. For this you need to install the
‘DeckLink SDK’ version 10.4 or above and copy the ‘dvp.dll’ runtime library to Blender’s
installation directory or to any other place where Blender can load a DLL from."""

	def __init__(self, format=None, capture=0):
		self.status = int()
		self.framerate = float()
		self.valid = bool()
		self.image = None
		self.size = (0,0)
		self.scale = bool()
		self.flip = bool()
		self.filter = None

	def play(self):
		"""Kick-off the capture after creation of the object."""
		return bool()

	def pause(self):
		"""Temporary stops the capture. Use play() to restart it."""
		return bool()

	def stop(self):
		"""Stops the capture."""
		return bool()


class Texture:
	"""Texture object."""

	def __init__(self, gameObj=None, materialID=0, textureID=0, textureObj=None):
		self.bindId = int()
		self.mipmap = bool()
		self.source = VideoFFmpeg()

	def close(self):
		"""Close dynamic texture and restore original."""

	def refresh(self, refresh_source, timestamp=-1.0):
		"""Refresh texture from source."""


class DeckLink:
	"""Certain DeckLink devices can be used to playback video: the host sends video frames regularly
for immediate or scheduled playback. The video feed is outputted on HDMI or SDI interfaces.
This class supports the immediate playback mode: it has a source attribute that is assigned
one of the source object in the bge.texture module. Refreshing the DeckLink object causes
the image source to be computed and sent to the DeckLink device for immediate transmission
on the output interfaces.  Keying is supported: it allows to composite the frame with an
input video feed that transits through the DeckLink card."""

	def __init__(self, cardIdx=0, format=""):
		self.source = VideoFFmpeg()
		self.right = VideoFFmpeg()
		self.keying = bool()
		self.level = int()
		self.extend = bool()

	def close(self):
		"""Close the DeckLink device and release all resources. After calling this method,
the object cannot be reactivated, it must be destroyed and a new DeckLink object
created from fresh to restart the output."""

	def refresh(self, refresh_source, ts):
		"""This method must be called frequently to update the output frame in the DeckLink device."""


class FilterBGR24:
	"""Source filter BGR24."""



class FilterBlueScreen:
	"""Filter for Blue Screen.
The RGB channels of the color are left unchanged, while the output alpha is obtained as follows:"""

	def __init__(self):
		self.color = [0,0,0]
		self.limits = [0,0]
		self.previous = FilterBGR24()


class FilterColor:
	"""Filter for color calculations.
The output color is obtained by multiplying the reduced 4x4 matrix with the input color
and adding the remaining column to the result."""

	def __init__(self):
		self.matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
		self.previous = FilterBGR24()


class FilterGray:
	"""Filter for gray scale effect.
Proportions of R, G and B contributions in the output gray scale are 28:151:77."""

	def __init__(self):
		self.previous = FilterBGR24()


class FilterLevel:
	"""Filter for levels calculations. Each output color component is obtained as follows:"""

	def __init__(self):
		self.levels = [[0,0],[0,0],[0,0],[0,0]]
		self.previous = FilterBGR24()


class FilterNormal:
	"""Normal map filter."""

	def __init__(self):
		self.colorIdx = int()
		self.depth = float()
		self.previous = FilterBGR24()


class FilterRGB24:
	"""Returns a new input filter object to be used with ImageBuff object when the image passed
to the ImageBuff.load() function has the 3-bytes pixel format BGR."""



class FilterRGBA32:
	"""Source filter RGBA32."""



def getLastError():
	"""Last error that occurred in a bge.texture function."""
	return str()

def imageToArray(image, mode):
	"""Returns a Buffer corresponding to the current image stored in a texture source object."""
	return bgl.Buffer()

def materialID(object, name):
	"""Returns a numeric value that can be used in Texture to create a dynamic texture."""
	return int()

def setLogFile(filename):
	"""Sets the name of a text file in which runtime error messages will be written, in addition to the printing
of the messages on the Python console. Only the runtime errors specific to the VideoTexture module
are written in that file, ordinary runtime time errors are not written."""
	return int()
SOURCE_ERROR = None
SOURCE_EMPTY = None
SOURCE_READY = None
SOURCE_PLAYING = None
SOURCE_STOPPED = None
IMB_BLEND_MIX = None
IMB_BLEND_ADD = None
IMB_BLEND_SUB = None
IMB_BLEND_MUL = None
IMB_BLEND_LIGHTEN = None
IMB_BLEND_DARKEN = None
IMB_BLEND_ERASE_ALPHA = None
IMB_BLEND_ADD_ALPHA = None
IMB_BLEND_OVERLAY = None
IMB_BLEND_HARDLIGHT = None
IMB_BLEND_COLORBURN = None
IMB_BLEND_LINEARBURN = None
IMB_BLEND_COLORDODGE = None
IMB_BLEND_SCREEN = None
IMB_BLEND_SOFTLIGHT = None
IMB_BLEND_PINLIGHT = None
IMB_BLEND_VIVIDLIGHT = None
IMB_BLEND_LINEARLIGHT = None
IMB_BLEND_DIFFERENCE = None
IMB_BLEND_EXCLUSION = None
IMB_BLEND_HUE = None
IMB_BLEND_SATURATION = None
IMB_BLEND_LUMINOSITY = None
IMB_BLEND_COLOR = None
IMB_BLEND_COPY = None
IMB_BLEND_COPY_RGB = None
IMB_BLEND_COPY_ALPHA = None
