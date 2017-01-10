Events
=========
Use this module for anything that sounds like event handling. 

.. note::
	
	This module is called ``event`` without the final "s" to avoid confusion with the module ``events`` of the BGE API.
	
.. data:: on_scene_added
	
	Callbacks for when a scene is added. You can then check wich scene with ``bge.logic.getCurrentScene()``

	:type: list
	
.. data:: on_scene_removed
	
	Callbacks for the next frame after a scene is removed. Doesn't trigger when a scene is automatically removed by closing the game. For that use ``__del__`` on a class.

	:type: list


.. data:: on_next_frame
	
	Callbacks that will be trigged on the next logic tick. The callback list is erased at the end of the current logic tick.

	:type: list
	
	
Key Bindings
--------------------

This module provides a simple yet powerful system to handle keyboard and any other kind of events as actions for owr behaviours.

The common problem: `How can I change the keys used by this or that component/script without modifing its source code`.

Another common problem: `How can I send an event to X specific component/script to make it think a key was pressed`.

This simple function will solve it all and more:

.. function:: keyBind(key)

	.. attribute:: key
		
		The key to be pressed. 
		
		:type: int (constant in ``bge.events``, one of the Keyboard Keys)
		
	:returns: Function checking the key specified. 
		
How to use it in a component:

.. code:: python

	from bge import events
	
	[...]
	
	def start(self, args):
		from core import event
		
		self.forward = event.keyBind(events.WKEY)
		self.backward = event.keyBind(events.SKEY)
		[...]
		
	def update(self):
		
		[...]
		
		x += float(self.forward()) - float(self.backward())
		
So with this we have saved in lines of code just to start with. But we could have done this just using a dictionary, the power of this system will start to shine on the following example, wich can be done anywere on your code. For even easier use we've make the following function too:

.. function:: keyPress(key)

	.. attribute:: key
		
		The key to be pressed. 
		
		:type: int (constant in ``bge.events``, one of the Keyboard Keys)
		
	:returns: True if the key its being pressed, false otherwise.


.. code:: python

	from core import event
	from bge import events, logic
	
	[...]
	
	com = object.components[n]
	
	#Changing a key for another
	com.forward = event.keyBind(events.UPARROWKEY)
	
	#Disabling a key
	com.forward = lambda: False
	
	#Any of two keys
	com.forward = lambda: event.keyPress(events.UPARROWKEY) or event.keyPress(events.UKEY)
	
	#The default key or another:
	default = com.forward
	com.forward = lambda: default() or event.keyPress(events.UPARROWKEY)
	
	#Two keys at the same time:
	com.forward = lambda: event.keyPress(events.UPARROWKEY) and event.keyPress(events.UKEY)
	
	#Joystick
	com.forward =  lambda: max(logic.joysticks[0].axisValues[1], 0)
	com.backward = lambda: min(logic.joysticks[0].axisValues[1], 0)
	
	#An external event
	myevents["forward"] = True
	[...]
	com.forward = lambda: myevents["forward"]
	
	#Another external event, a game property
	com.forward = lambda: obj["forward"]
	
	#This one even lets us use logic bricks to configure keys, for example doing:
	#[Keyboard] -> [And] -> [Property: Mode(Level), Property("forward")] 
	
	
		