
def createConstraint(physicsid_1, physicsid_2, constraint_type, pivot_x=0.0, pivot_y=0.0, pivot_z=0.0, axis_x=0.0, axis_y=0.0, axis_z=0.0, flag=0):
	"""Creates a constraint."""
	return self

def exportBulletFile(filename):
	"""Exports a file representing the dynamics world (usually using .bullet extension)."""

def getAppliedImpulse(constraintId):
	return float()

def getVehicleConstraint(constraintId):
	import bge
	return bge.types.KX_VehicleWrapper()

def getCharacter(gameobj):
	import bge
	return bge.types.KX_CharacterWrapper()

def removeConstraint(constraintId):
	"""Removes a constraint."""

def setCcdMode(ccdMode):
	"""Note"""

def setContactBreakingTreshold(breakingTreshold):
	"""Note"""

def setDeactivationAngularTreshold(angularTreshold):
	"""Sets the angular velocity treshold."""

def setDeactivationLinearTreshold(linearTreshold):
	"""Sets the linear velocity treshold."""

def setDeactivationTime(time):
	"""Sets the time after which a resting rigidbody gets deactived."""

def setDebugMode(mode):
	"""Sets the debug mode."""

def setGravity(x, y, z):
	"""Sets the gravity force."""

def setLinearAirDamping(damping):
	"""Note"""

def setNumIterations(numiter):
	"""Sets the number of iterations for an iterative constraint solver."""

def setNumTimeSubSteps(numsubstep):
	"""Sets the number of substeps for each physics proceed. Tradeoff quality for performance."""

def setSolverDamping(damping):
	"""Note"""

def setSolverTau(tau):
	"""Note"""

def setSolverType(solverType):
	"""Note"""

def setSorConstant(sor):
	"""Note"""

def setUseEpa(epa):
	"""Note"""
DBG_NODEBUG = None
DBG_DRAWWIREFRAME = None
DBG_DRAWAABB = None
DBG_DRAWFREATURESTEXT = None
DBG_DRAWCONTACTPOINTS = None
DBG_NOHELPTEXT = None
DBG_DRAWTEXT = None
DBG_PROFILETIMINGS = None
DBG_ENABLESATCOMPARISION = None
DBG_DISABLEBULLETLCP = None
DBG_ENABLECCD = None
DBG_DRAWCONSTRAINTS = None
DBG_DRAWCONSTRAINTLIMITS = None
DBG_FASTWIREFRAME = None
POINTTOPOINT_CONSTRAINT = None
LINEHINGE_CONSTRAINT = None
ANGULAR_CONSTRAINT = None
CONETWIST_CONSTRAINT = None
VEHICLE_CONSTRAINT = None
GENERIC_6DOF_CONSTRAINT = None
