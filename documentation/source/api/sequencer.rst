Sequencer
=========

The sequencer is a system to make dynamic animations using function callbacks. It allows us to animate anything that can be accesed from Python. It is nesscesary when triying to animate some components of BGECore (e.j: music, sprites, widgets). This module is not intended to replace current Blender Game Engine animation system and should not be used for bones or cinematics.

.. code-block:: python

	from core import behavior, key, sequencer

	class Grenade(behavior.Object):
		[...]
		
		def onKeyRelease(self, keys):
			if key.E in keys: sequencer.Wait(5, self.expolde) 
			[...]
			
		def explode(self):
			print("KABUUM!")
			
Callbacks are stored either in ``module.low_frequency_callbacks`` or ``module.height_frequecy_callbacks``. The default frquency of those are 10Hz and 50Hz.
			
.. autoclass:: core.sequencer.Wait
	:members:
	
.. autoclass:: core.sequencer.LinearInterpolation
	:members:
	
.. autoclass:: core.sequencer.AlphaFade
	:members:
