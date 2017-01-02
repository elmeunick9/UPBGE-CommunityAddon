import json, bge

video_playback_list = []
low_frequency_callbacks = []
height_frequency_callbacks = []

LOW_FREQUENCY_TICK = 0.06
HEIGHT_FREQUENCY_TICK = 0.02

project_data = None

def loadProjectFile():
	path = bge.logic.expandPath('//../project.json')

	global project_data
	try:
		with open(path) as json_file: project_data = json.load(json_file)
	except Exception as e: 
		print(str(e))
		
def __init__():
	loadProjectFile()
	
__init__()