from . import glsl, module, utils, sequencer
import bge

import sys
sys.path.append(bge.logic.expandPath('//core/com'))

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

#To avoid documentation (Sphinx) errors, we don't initialize anything.
if str(type(bge)) != "<class 'sphinx.ext.autodoc._MockModule'>":
	execute_stored_scripts()
else:
	from . import com
	


import time

last_time = [time.time(), time.time()]
def loop():

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
		

