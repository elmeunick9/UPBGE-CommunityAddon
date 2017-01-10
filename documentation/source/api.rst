Python API
================================================================================
The new Python API, `core`, provides extra functionality to the BGE API.

.. currentmodule:: core

.. toctree::
  :maxdepth: 2
  :hidden:

  api/event
  api/media
  api/utils
  api/sequencer
  api/filter2D

**Module**

The ``core.module`` module provides acces to important references that can be used anywere.
	
.. data:: core.module.low_frequency_callbacks

	A list of functions that will be called after each ``LOW_FREQUECY_TICK``. Functions are called with the argument ``time``, a float representing the amount of time since the last call.
	
.. data:: core.module.height_frequency_callbacks

	A list of functions that will be called after each ``HEIGHT_FREQUECY_TICK``. Functions are called with the argument ``time``, a float representing the amount of time since the last call.



  
