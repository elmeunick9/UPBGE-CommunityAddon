globalDict = {}
keyboard = None
mouse = None
joysticks = []


def getCurrentController():
	"""Gets the Python controller associated with this Python script."""
	import bge
	return bge.types.SCA_PythonController()

def getCurrentScene():
	"""Gets the current Scene."""
	import bge
	return bge.types.KX_Scene()

def getSceneList():
	"""Gets a list of the current scenes loaded in the game engine."""
	import bge
	return bge.types.CListValue(bge.types.KX_Scene)

def getInactiveSceneNames():
	"""Gets a list of the scene’s names not loaded in the game engine."""
	import bge
	return bge.types.CListValue(str)

def loadGlobalDict():
	"""Loads bge.logic.globalDict from a file."""

def saveGlobalDict():
	"""Saves bge.logic.globalDict to a file."""

def startGame(blend):
	"""Loads the blend file."""

def endGame():
	"""Ends the current game."""

def restartGame():
	"""Restarts the current game by reloading the .blend file (the last saved version, not what is currently running)."""

def LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, async=False):
	"""Converts the all of the datablocks of the given type from the given blend."""
	return self

def LibNew(name, type, data):
	"""Uses existing datablock data and loads in as a new library."""

def LibFree(name):
	"""Frees a library, removing all objects and meshes from the currently active scenes."""

def LibList():
	"""Returns a list of currently loaded libraries."""
	return [str()]

def addScene(name, overlay=1):
	"""Loads a scene into the game engine."""

def sendMessage(subject, body="", to="", message_from=""):
	"""Sends a message to sensors in any active scene."""

def setGravity(gravity):
	"""Sets the world gravity."""

def getMaxLogicFrame():
	"""Gets the maximum number of logic frames per render frame."""
	return int()

def setMaxLogicFrame(maxlogic):
	"""Sets the maximum number of logic frames that are executed per render frame.
This does not affect the physic system that still runs at full frame rate."""

def getMaxPhysicsFrame():
	"""Gets the maximum number of physics frames per render frame."""
	return int()

def setMaxPhysicsFrame(maxphysics):
	"""Sets the maximum number of physics timestep that are executed per render frame.
Higher value allows physics to keep up with realtime even if graphics slows down the game.
Physics timestep is fixed and equal to 1/tickrate (see setLogicTicRate)
maxphysics/ticrate is the maximum delay of the renderer that physics can compensate."""

def getLogicTicRate():
	"""Gets the logic update frequency."""
	return float()

def setLogicTicRate(ticrate):
	"""Sets the logic update frequency."""

def getPhysicsTicRate():
	"""Gets the physics update frequency"""
	return float()

def setPhysicsTicRate(ticrate):
	"""Sets the physics update frequency"""

def getAnimRecordFrame():
	"""Gets the current frame number used for recording animations. This
number is incremented automatically by Blender when the “Record
animation” feature is turned on."""
	return int()

def setAnimRecordFrame(framenr):
	"""Sets the current frame number used for recording animations. This
number is automatically incremented by Blender when the “Record
animation” feature is turned on."""

def getExitKey():
	"""Gets the key used to exit the game engine"""
	return int()

def setExitKey(key):
	"""Sets the key used to exit the game engine"""

def NextFrame():
	"""Render next frame (if Python has control)"""

def setRender(render):
	"""Sets the global flag that controls the render of the scene.
If True, the render is done after the logic frame.
If False, the render is skipped and another logic frame starts immediately."""

def getRender():
	"""Get the current value of the global render flag"""
	return bool()

def getClockTime():
	"""Get the current BGE render time, in seconds. The BGE render time is the
simulation time corresponding to the next scene that will be rendered."""
	return float()

def getFrameTime():
	"""Get the current BGE frame time, in seconds. The BGE frame time is the
simulation time corresponding to the current call of the logic system.
Generally speaking, it is what the user is interested in."""
	return float()

def getRealTime():
	"""Get the number of real (system-clock) seconds elapsed since the beginning
of the simulation."""
	return float()

def getTimeScale():
	"""Get the time multiplier between real-time and simulation time. The default
value is 1.0. A value greater than 1.0 means that the simulation is going
faster than real-time, a value lower than 1.0 means that the simulation is
going slower than real-time."""
	return float()

def setTimeScale(time_scale):
	"""Set the time multiplier between real-time and simulation time. A value
greater than 1.0 means that the simulation is going faster than real-time,
a value lower than 1.0 means that the simulation is going slower than
real-time. Note that a too large value may lead to some physics
instabilities."""

def getUseExternalClock():
	"""Get if the BGE use the inner BGE clock, or rely or on an external
clock. The default is to use the inner BGE clock."""
	return bool()

def setUseExternalClock(use_external_clock):
	"""Set if the BGE use the inner BGE clock, or rely or on an external
clock. If the user selects the use of an external clock, he should call
regularly the setClockTime method."""

def setClockTime(new_time):
	"""Set the next value of the simulation clock. It is preferable to use this
method from a custom main function in python, as calling it in the logic
block can easily lead to a blocked system (if the time does not advance
enough to run at least the next logic step)."""

def expandPath(path):
	"""Converts a blender internal path into a proper file system path."""
	return str()

def getAverageFrameRate():
	"""Gets the estimated/average framerate for all the active scenes, not only the current scene."""
	return float()

def getBlendFileList(path = "//"):
	"""Returns a list of blend files in the same directory as the open blend file, or from using the option argument."""
	return list()

def getRandomFloat():
	"""Returns a random floating point value in the range [0 - 1)"""

def PrintGLInfo():
	"""Prints GL Extension Info into the console"""

def PrintMemInfo():
	"""Prints engine statistics into the console"""

def getProfileInfo():
	"""Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time."""
KX_TRUE = None
KX_FALSE = None
KX_SENSOR_INACTIVE = None
KX_SENSOR_JUST_ACTIVATED = None
KX_SENSOR_ACTIVE = None
KX_SENSOR_JUST_DEACTIVATED = None
KX_ARMSENSOR_STATE_CHANGED = 0
KX_ARMSENSOR_LIN_ERROR_BELOW = 1
KX_ARMSENSOR_LIN_ERROR_ABOVE = 2
KX_ARMSENSOR_ROT_ERROR_BELOW = 3
KX_ARMSENSOR_ROT_ERROR_ABOVE = 4
KX_PROPSENSOR_EQUAL = 1
KX_PROPSENSOR_NOTEQUAL = 2
KX_PROPSENSOR_INTERVAL = 3
KX_PROPSENSOR_CHANGED = 4
KX_PROPSENSOR_EXPRESSION = 5
KX_PROPSENSOR_LESSTHAN = 6
KX_PROPSENSOR_GREATERTHAN = 7
KX_RADAR_AXIS_POS_X = None
KX_RADAR_AXIS_POS_Y = None
KX_RADAR_AXIS_POS_Z = None
KX_RADAR_AXIS_NEG_X = None
KX_RADAR_AXIS_NEG_Y = None
KX_RADAR_AXIS_NEG_Z = None
KX_RAY_AXIS_POS_X = None
KX_RAY_AXIS_POS_Y = None
KX_RAY_AXIS_POS_Z = None
KX_RAY_AXIS_NEG_X = None
KX_RAY_AXIS_NEG_Y = None
KX_RAY_AXIS_NEG_Z = None
KX_ACTIONACT_PLAY = None
KX_ACTIONACT_PINGPONG = None
KX_ACTIONACT_FLIPPER = None
KX_ACTIONACT_LOOPSTOP = None
KX_ACTIONACT_LOOPEND = None
KX_ACTIONACT_PROPERTY = None
KX_ACT_ARMATURE_RUN = 0
KX_ACT_ARMATURE_ENABLE = 1
KX_ACT_ARMATURE_DISABLE = 2
KX_ACT_ARMATURE_SETTARGET = 3
KX_ACT_ARMATURE_SETWEIGHT = 4
KX_ACT_ARMATURE_SETINFLUENCE = 5
KX_CONSTRAINTACT_NORMAL = None
KX_CONSTRAINTACT_DISTANCE = None
KX_CONSTRAINTACT_LOCAL = None
KX_CONSTRAINTACT_DOROTFH = None
KX_CONSTRAINTACT_MATERIAL = None
KX_CONSTRAINTACT_PERMANENT = None
KX_CONSTRAINTACT_LOCX = None
KX_CONSTRAINTACT_LOCY = None
KX_CONSTRAINTACT_LOCZ = None
KX_CONSTRAINTACT_ROTX = None
KX_CONSTRAINTACT_ROTY = None
KX_CONSTRAINTACT_ROTZ = None
KX_CONSTRAINTACT_DIRNX = None
KX_CONSTRAINTACT_DIRNY = None
KX_CONSTRAINTACT_DIRNZ = None
KX_CONSTRAINTACT_DIRPX = None
KX_CONSTRAINTACT_DIRPY = None
KX_CONSTRAINTACT_DIRPZ = None
KX_CONSTRAINTACT_ORIX = None
KX_CONSTRAINTACT_ORIY = None
KX_CONSTRAINTACT_ORIZ = None
KX_CONSTRAINTACT_FHNX = None
KX_CONSTRAINTACT_FHNY = None
KX_CONSTRAINTACT_FHNZ = None
KX_CONSTRAINTACT_FHPX = None
KX_CONSTRAINTACT_FHPY = None
KX_CONSTRAINTACT_FHPZ = None
KX_DYN_RESTORE_DYNAMICS = None
KX_DYN_DISABLE_DYNAMICS = None
KX_DYN_ENABLE_RIGID_BODY = None
KX_DYN_DISABLE_RIGID_BODY = None
KX_DYN_SET_MASS = None
KX_GAME_LOAD = None
KX_GAME_START = None
KX_GAME_RESTART = None
KX_GAME_QUIT = None
KX_GAME_SAVECFG = None
KX_GAME_LOADCFG = None
KX_ACT_MOUSE_OBJECT_AXIS_X = None
KX_ACT_MOUSE_OBJECT_AXIS_Y = None
KX_ACT_MOUSE_OBJECT_AXIS_Z = None
KX_PARENT_REMOVE = None
KX_PARENT_SET = None
KX_RANDOMACT_BOOL_CONST = None
KX_RANDOMACT_BOOL_UNIFORM = None
KX_RANDOMACT_BOOL_BERNOUILLI = None
KX_RANDOMACT_INT_CONST = None
KX_RANDOMACT_INT_UNIFORM = None
KX_RANDOMACT_INT_POISSON = None
KX_RANDOMACT_FLOAT_CONST = None
KX_RANDOMACT_FLOAT_UNIFORM = None
KX_RANDOMACT_FLOAT_NORMAL = None
KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL = None
KX_SCENE_RESTART = None
KX_SCENE_SET_SCENE = None
KX_SCENE_SET_CAMERA = None
KX_SCENE_ADD_FRONT_SCENE = None
KX_SCENE_ADD_BACK_SCENE = None
KX_SCENE_REMOVE_SCENE = None
KX_SCENE_SUSPEND = None
KX_SCENE_RESUME = None
KX_SOUNDACT_PLAYSTOP = 1
KX_SOUNDACT_PLAYEND = 2
KX_SOUNDACT_LOOPSTOP = 3
KX_SOUNDACT_LOOPEND = 4
KX_SOUNDACT_LOOPBIDIRECTIONAL = 5
KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP = 6
KX_STEERING_SEEK = 1
KX_STEERING_FLEE = 2
KX_STEERING_PATHFOLLOWING = 3
KX_TRACK_UPAXIS_POS_X = None
KX_TRACK_UPAXIS_POS_Y = None
KX_TRACK_UPAXIS_POS_Z = None
KX_TRACK_TRAXIS_POS_X = None
KX_TRACK_TRAXIS_POS_Y = None
KX_TRACK_TRAXIS_POS_Z = None
KX_TRACK_TRAXIS_NEG_X = None
KX_TRACK_TRAXIS_NEG_Y = None
KX_TRACK_TRAXIS_NEG_Z = None
RAS_2DFILTER_BLUR = 2
RAS_2DFILTER_CUSTOMFILTER = 12
RAS_2DFILTER_DILATION = 4
RAS_2DFILTER_DISABLED = -1
RAS_2DFILTER_ENABLED = -2
RAS_2DFILTER_EROSION = 5
RAS_2DFILTER_GRAYSCALE = 9
RAS_2DFILTER_INVERT = 11
RAS_2DFILTER_LAPLACIAN = 6
RAS_2DFILTER_MOTIONBLUR = 1
RAS_2DFILTER_NOFILTER = 0
RAS_2DFILTER_PREWITT = 8
RAS_2DFILTER_SEPIA = 10
RAS_2DFILTER_SHARPEN = 3
RAS_2DFILTER_SOBEL = 7
ROT_MODE_QUAT = 0
ROT_MODE_XYZ = 1
ROT_MODE_XZY = 2
ROT_MODE_YXZ = 3
ROT_MODE_YZX = 4
ROT_MODE_ZXY = 5
ROT_MODE_ZYX = 6
CONSTRAINT_TYPE_TRACKTO = None
CONSTRAINT_TYPE_KINEMATIC = None
CONSTRAINT_TYPE_ROTLIKE = None
CONSTRAINT_TYPE_LOCLIKE = None
CONSTRAINT_TYPE_MINMAX = None
CONSTRAINT_TYPE_SIZELIKE = None
CONSTRAINT_TYPE_LOCKTRACK = None
CONSTRAINT_TYPE_STRETCHTO = None
CONSTRAINT_TYPE_CLAMPTO = None
CONSTRAINT_TYPE_TRANSFORM = None
CONSTRAINT_TYPE_DISTLIMIT = None
CONSTRAINT_IK_COPYPOSE = 0
CONSTRAINT_IK_DISTANCE = 1
CONSTRAINT_IK_FLAG_TIP = 1
CONSTRAINT_IK_FLAG_ROT = 2
CONSTRAINT_IK_FLAG_STRETCH = 16
CONSTRAINT_IK_FLAG_POS = 32
CONSTRAINT_IK_MODE_INSIDE = 0
CONSTRAINT_IK_MODE_OUTSIDE = 1
CONSTRAINT_IK_MODE_ONSURFACE = 2
BL_DST_ALPHA = None
BL_DST_COLOR = None
BL_ONE = None
BL_ONE_MINUS_DST_ALPHA = None
BL_ONE_MINUS_DST_COLOR = None
BL_ONE_MINUS_SRC_ALPHA = None
BL_ONE_MINUS_SRC_COLOR = None
BL_SRC_ALPHA = None
BL_SRC_ALPHA_SATURATE = None
BL_SRC_COLOR = None
BL_ZERO = None
KX_INPUT_NONE = None
KX_INPUT_JUST_ACTIVATED = None
KX_INPUT_ACTIVE = None
KX_INPUT_JUST_RELEASED = None
KX_ACTION_MODE_PLAY = 0
KX_ACTION_MODE_LOOP = 1
KX_ACTION_MODE_PING_PONG = 2
KX_ACTION_BLEND_BLEND = 0
KX_ACTION_BLEND_ADD = 1
KX_MOUSE_BUT_LEFT = None
KX_MOUSE_BUT_MIDDLE = None
KX_MOUSE_BUT_RIGHT = None
RM_WALLS = None
RM_POLYS = None
RM_TRIS = None
VIEWMATRIX = None
VIEWMATRIX_INVERSE = None
VIEWMATRIX_INVERSETRANSPOSE = None
VIEWMATRIX_TRANSPOSE = None
MODELMATRIX = None
MODELMATRIX_INVERSE = None
MODELMATRIX_INVERSETRANSPOSE = None
MODELMATRIX_TRANSPOSE = None
MODELVIEWMATRIX = None
MODELVIEWMATRIX_INVERSE = None
MODELVIEWMATRIX_INVERSETRANSPOSE = None
MODELVIEWMATRIX_TRANSPOSE = None
CAM_POS = None
CONSTANT_TIMER = None
EYE = None
SHD_TANGENT = None
KX_STATE1 = None
KX_STATE2 = None
KX_STATE3 = None
KX_STATE4 = None
KX_STATE5 = None
KX_STATE6 = None
KX_STATE7 = None
KX_STATE8 = None
KX_STATE9 = None
KX_STATE10 = None
KX_STATE11 = None
KX_STATE12 = None
KX_STATE13 = None
KX_STATE14 = None
KX_STATE15 = None
KX_STATE16 = None
KX_STATE17 = None
KX_STATE18 = None
KX_STATE19 = None
KX_STATE20 = None
KX_STATE21 = None
KX_STATE22 = None
KX_STATE23 = None
KX_STATE24 = None
KX_STATE25 = None
KX_STATE26 = None
KX_STATE27 = None
KX_STATE28 = None
KX_STATE29 = None
KX_STATE30 = None
KX_STATE_OP_CLR = 0
KX_STATE_OP_CPY = 1
KX_STATE_OP_NEG = 2
KX_STATE_OP_SET = 3
