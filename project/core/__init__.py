from . import glsl, module, utils, sequencer, events
import bge

import sys
sys.path.append(bge.logic.expandPath('//core/com'))

if str(type(bge)) == "<class 'sphinx.ext.autodoc._MockModule'>": from . import com

def execute_stored_scripts():
	scnn = bge.logic.getCurrentScene().name
	if not "__reserved__" in bge.logic.globalDict: bge.logic.globalDict["__reserved__"] = {"filter2D": {}}
	fd = bge.logic.globalDict["__reserved__"]["filter2D"]
	if not scnn in fd: fd[scnn] = {}
	else: return
	
	try:
		scripts = module.project_data["bge-project"]["settings"]["filter2D"][bge.logic.getCurrentScene().name]
		for key, script in scripts.items():
			code = compile(script, '<string>', 'exec')
			exec(code)
			
	except KeyError: pass
	
def clean_stored_scripts():
	scnn = bge.logic.getCurrentScene().name
	fd = bge.logic.globalDict["__reserved__"]["filter2D"]
	del fd[scnn]
	
import time, collections
last_time = [time.time(), time.time()]

scene_owners = collections.OrderedDict()
scene_onames = {}
count = 0
def loop(cont):
	global scene_owners, scene_onames, count

	#Poll scene status
	coname = cont.owner.name
	if not coname in scene_owners:						#Scene loaded
		scene_owners[coname] = count
		scene_onames[coname] = cont.owner.scene.name
		execute_stored_scripts()
		for x in events.on_scene_added: x(cont.owner.scene.name)
	else:
		if list(scene_owners.items())[0][0] == coname:
			count += 1 #Will never overflow on Python3
			for own in scene_owners:
				if scene_owners[own] != count - 1:		#Scene deleted last frame
					clean_stored_scripts()
					del scene_owners[coname]
					for x in events.on_scene_removed: x(scene_onames[coname])
			
		scene_owners[coname] = count
		
	#Special case to cleanly remove 2DFilters when exiting the game form the Viewport, if exit in another way the won't be cleanly removed.
	
		


	next_frame_callbacks = events.on_next_frame[:]
	del events.on_next_frame[:]
	for x in next_frame_callbacks: x()
	
	#Fequency Callbacks
	global last_time

	t = time.time()
	dtA, dtB = t - last_time[0], t - last_time[1]
	
	if dtA >= module.LOW_FREQUENCY_TICK:
		last_time[0] = t
		for call in module.low_frequency_callbacks: call(dtA)
		for v in module.video_playback_list: v.updateVideo()

	if dtB >= module.HEIGHT_FREQUENCY_TICK:
		last_time[1] = t
		for call in module.height_frequency_callbacks: call(dtB)	
		

