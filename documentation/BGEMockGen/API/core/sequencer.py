
class Wait:
	"""Waits a certain amount of time, then calls the callback function."""

	def __init__(self, time=None, callback=None):
		self.x = float()

	def delete(self):
		"""Deletes/Stops the effect. Automatically called once x >= time."""


class LinearInterpolation:
	"""Makes a linear interpolation over time, uses a callback to apply changes."""

	def __init__(self, A=None, B=None, time=None, callback=None, final=None, transform=False):
		self.x = float()

	def delete(self):
		"""Deletes/Stops the interpolation. Automatically called once x >= time."""


class AlphaFade:
	"""Makes a object fadeIn, wait, and fadeOut."""

	def __init__(self, obj=None, A=None, B=None, xtime=None, ytime=None, mtime=0, xcallback=None, mcallback=None, ycallback=None):
		self.x = float()

	def xchange(self, x):
		"""The callback that changes the color of the object. If the class is extended, this method can be overwritten to modify any property."""

	def delete(self):
		"""Deletes/Stops the effect. Automatically called once x >= xtime+mtime+ytime."""

