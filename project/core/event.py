on_scene_added = []
on_scene_removed = []
on_next_frame = []

import bge

def keyPress(key):
	return bge.logic.keyboard.inputs[key].status[0] == bge.logic.KX_INPUT_ACTIVE

def keyBind(key):
	def keyAction():
		return bge.logic.keyboard.inputs[key].status[0] == bge.logic.KX_INPUT_ACTIVE
		
	return keyAction