
import mathutils

inf = 0
class CListValue:
    def __init__(self, ctype):
        self.__ret__ = ctype
        self.__i__ = None
        self.__itf__ = False

    def __instanceme__(self):
        if self.__i__ == None:
            self.__i__ = self.__ret__()
        return self.__i__

    def __getitem__(self, key): return self.__instanceme__()
    def __setitem__(self, key, val): return self.__instanceme__()
    def get(self, key): return self.__instanceme__()

    def __iter__(self): return self
    def __next__(self):
        self.__itf__ = not self.__itf__
        if self.__itf__: return self.__instanceme__()
        else: raise StopIteration

class PyObjectPlus:
	"""PyObjectPlus base class of most other types in the Game Engine."""

	def __init__(self):
		self.invalid = bool()


class CValue(PyObjectPlus):
	"""This class is a basis for other classes."""

	def __init__(self):
		self.name = str()


class BL_Shader(PyObjectPlus):
	"""BL_Shader GLSL shaders."""

	def __init__(self):
		self.enabled = bool()
		self.objectCallbacks = list()
		self.bindCallbacks = list()

	def setUniformfv(self, name, fList):
		"""Set a uniform with a list of float values"""

	def delSource(self):
		"""Clear the shader. Use this method before the source is changed with setSource."""

	def getFragmentProg(self):
		"""Returns the fragment program."""
		return str()

	def getVertexProg(self):
		"""Get the vertex program."""
		return str()

	def isValid(self):
		"""Check if the shader is valid."""
		return bool()

	def setAttrib(self, enum):
		"""Set attribute location. (The parameter is ignored a.t.m. and the value of “tangent” is always used.)"""

	def setSampler(self, name, index):
		"""Set uniform texture sample index."""

	def setSource(self, vertexProgram, fragmentProgram, apply):
		"""Set the vertex and fragment programs"""

	def setSourceList(self, sources, apply):
		"""Set the vertex, fragment and geometry shader programs."""

	def setUniform1f(self, name, fx):
		"""Set a uniform with 1 float value."""

	def setUniform1i(self, name, ix):
		"""Set a uniform with an integer value."""

	def setUniform2f(self, name, fx, fy):
		"""Set a uniform with 2 float values"""

	def setUniform2i(self, name, ix, iy):
		"""Set a uniform with 2 integer values"""

	def setUniform3f(self, name, fx, fy, fz):
		"""Set a uniform with 3 float values."""

	def setUniform3i(self, name, ix, iy, iz):
		"""Set a uniform with 3 integer values"""

	def setUniform4f(self, name, fx, fy, fz, fw):
		"""Set a uniform with 4 float values."""

	def setUniform4i(self, name, ix, iy, iz, iw):
		"""Set a uniform with 4 integer values"""

	def setUniformDef(self, name, type):
		"""Define a new uniform"""

	def setUniformMatrix3(self, name, mat, transpose):
		"""Set a uniform with a 3x3 matrix value"""

	def setUniformMatrix4(self, name, mat, transpose):
		"""Set a uniform with a 4x4 matrix value"""

	def setUniformiv(self, name, iList):
		"""Set a uniform with a list of integer values"""

	def setUniformEyef(self, name):
		"""Set a uniform with a float value that reflects the eye being render in stereo mode:
0.0 for the left eye, 0.5 for the right eye. In non stereo mode, the value of the uniform
is fixed to 0.0. The typical use of this uniform is in stereo mode to sample stereo textures
containing the left and right eye images in a top-bottom order."""

	def validate(self):
		"""Validate the shader object."""


class SCA_IObject(CValue):
	"""This class has no python functions"""



class KX_BoundingBox(PyObjectPlus):
	"""A bounding volume box of a game object. Used to get and alterate the volume box or AABB."""

	def __init__(self):
		self.min = mathutils.Vector()
		self.max = mathutils.Vector()
		self.center = mathutils.Vector()
		self.radius = float()
		self.autoUpdate = bool()


class SCA_ILogicBrick(CValue):
	"""Base class for all logic bricks."""

	def __init__(self):
		self.executePriority = int()
		self.owner = KX_GameObject()
		self.name = str()


class SCA_ISensor(SCA_ILogicBrick):
	"""Base class for all sensor logic bricks."""

	def __init__(self):
		self.usePosPulseMode = bool()
		self.useNegPulseMode = bool()
		self.frequency = int()
		self.skippedTicks = int()
		self.level = bool()
		self.tap = bool()
		self.invert = bool()
		self.triggered = bool()
		self.positive = bool()
		self.pos_ticks = int()
		self.neg_ticks = int()
		self.status = int()

	def reset(self):
		"""Reset sensor internal state, effect depends on the type of sensor and settings."""


class KX_PythonComponent(CValue):
	"""Python component can be compared to python logic bricks with parameters.
The python component is a script loaded in the UI, this script defined a component class by inheriting from KX_PythonComponent.
This class must contain a dictionary of properties: args and two default functions: start() and update()."""

	def __init__(self):
		self.object = KX_GameObject()
		self.args = dict()

	def start(self, args):
		"""Initialize the component."""

	def update(self):
		"""Process the logic of the component."""


class KX_LodLevel(PyObjectPlus):
	"""A single lod level for a game object lod manager."""

	def __init__(self):
		self.mesh = None
		self.level = int()
		self.distance = float()
		self.hysteresis = float()
		self.useMesh = bool()
		self.useMaterial = bool()
		self.useHysteresis = bool()


class KX_LodManager(PyObjectPlus):
	"""This class contains a list of all levels of detail used by a game object."""

	def __init__(self):
		self.levels = CListValue(KX_LodLevel)
		self.distanceFactor = float()


class KX_GameObject(SCA_IObject):
	"""All game objects are derived from this class."""

	def __init__(self):
		self.name = str()
		self.mass = float()
		self.isSuspendDynamics = bool()
		self.linearDamping = float()
		self.angularDamping = float()
		self.linVelocityMin = float()
		self.linVelocityMax = float()
		self.angularVelocityMin = float()
		self.angularVelocityMax = float()
		self.localInertia = mathutils.Vector()
		self.parent = self
		self.groupMembers = CListValue(KX_GameObject)
		self.groupObject = self
		self.collisionGroup = int()
		self.collisionMask = int()
		self.collisionCallbacks = list()
		self.scene = None
		self.visible = bool()
		self.layer = int()
		self.cullingBox = KX_BoundingBox()
		self.culled = bool()
		self.color = mathutils.Vector()
		self.occlusion = bool()
		self.position = mathutils.Vector()
		self.orientation = mathutils.Matrix()
		self.scaling = mathutils.Vector()
		self.localOrientation = mathutils.Matrix()
		self.worldOrientation = mathutils.Matrix()
		self.localScale = mathutils.Vector()
		self.worldScale = mathutils.Vector()
		self.localPosition = mathutils.Vector()
		self.worldPosition = mathutils.Vector()
		self.localTransform = mathutils.Matrix()
		self.worldTransform = mathutils.Matrix()
		self.localLinearVelocity = mathutils.Vector()
		self.worldLinearVelocity = mathutils.Vector()
		self.localAngularVelocity = mathutils.Vector()
		self.worldAngularVelocity = mathutils.Vector()
		self.timeOffset = float()
		self.state = int()
		self.meshes = CListValue(KX_MeshProxy)
		self.sensors = list()
		self.controllers = CListValue(SCA_ISensor)
		self.actuators = list()
		self.attrDict = dict()
		self.components = CListValue(KX_PythonComponent)
		self.children = CListValue(KX_GameObject)
		self.childrenRecursive = CListValue(KX_GameObject)
		self.life = float()
		self.debug = bool()
		self.debugRecursive = bool()
		self.currentLodLevel = int()
		self.lodManager = KX_LodManager()

	def endObject(self):
		"""Delete this object, can be used in place of the EndObject Actuator."""

	def replaceMesh(self, mesh, useDisplayMesh=True, usePhysicsMesh=False):
		"""Replace the mesh of this object with a new mesh. This works the same was as the actuator."""

	def setVisible(self, visible, recursive):
		"""Sets the game object’s visible flag."""

	def setOcclusion(self, occlusion, recursive):
		"""Sets the game object’s occlusion capability."""

	def alignAxisToVect(self, vect, axis=2, factor=1.0):
		"""Aligns any of the game object’s axis along the given vector."""

	def getAxisVect(self, vect):
		"""Returns the axis vector rotates by the object’s worldspace orientation.
This is the equivalent of multiplying the vector by the orientation matrix."""
		return mathutils.Vector()

	def applyMovement(self, movement, local=False):
		"""Sets the game object’s movement."""

	def applyRotation(self, rotation, local=False):
		"""Sets the game object’s rotation."""

	def applyForce(self, force, local=False):
		"""Sets the game object’s force."""

	def applyTorque(self, torque, local=False):
		"""Sets the game object’s torque."""

	def getLinearVelocity(self, local=False):
		"""Gets the game object’s linear velocity."""
		return mathutils.Vector()

	def setLinearVelocity(self, velocity, local=False):
		"""Sets the game object’s linear velocity."""

	def getAngularVelocity(self, local=False):
		"""Gets the game object’s angular velocity."""
		return mathutils.Vector()

	def setAngularVelocity(self, velocity, local=False):
		"""Sets the game object’s angular velocity."""

	def getVelocity(self, point=(0, 0, 0)):
		"""Gets the game object’s velocity at the specified point."""
		return mathutils.Vector()

	def getReactionForce(self):
		"""Gets the game object’s reaction force."""
		return mathutils.Vector()

	def applyImpulse(self, point, impulse, local=False):
		"""Applies an impulse to the game object."""

	def setDamping(self, linear_damping, angular_damping):
		"""Sets both the linearDamping and angularDamping simultaneously. This is more efficient than setting both properties individually."""

	def suspendPhysics(self):
		"""Suspends physics for this object."""

	def restorePhysics(self):
		"""Resumes physics for this object. Also reinstates collisions."""

	def suspendDynamics(self, ghost):
		"""Suspends dynamics physics for this object."""

	def restoreDynamics(self):
		"""Resumes dynamics physics for this object. Also reinstates collisions; the object will no longer be a ghost."""

	def enableRigidBody(self):
		"""Enables rigid body physics for this object."""

	def disableRigidBody(self):
		"""Disables rigid body physics for this object."""

	def setParent(self, parent, compound=True, ghost=True):
		"""Sets this object’s parent.
Control the shape status with the optional compound and ghost parameters:"""

	def removeParent(self):
		"""Removes this objects parent."""

	def getPhysicsId(self):
		"""Returns the user data object associated with this game object’s physics controller."""

	def getPropertyNames(self):
		"""Gets a list of all property names."""
		return list()

	def getDistanceTo(self, other):
		return float()

	def getVectTo(self, other):
		"""Returns the vector and the distance to another object or point.
The vector is normalized unless the distance is 0, in which a zero length vector is returned."""
		return (float, (0,0,0), (0,0,0))

	def rayCastTo(self, other, dist, prop):
		"""Look towards another point/object and find first object hit within dist that matches prop."""
		return self

	def rayCast(self, objto, objfrom, dist, prop, face, xray, poly, mask):
		"""Look from a point/object to another point/object and find first object hit within dist that matches prop.
if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit.
if poly is 1, returns a 4-tuple with in addition a KX_PolyProxy as 4th element.
if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element."""
		return (KX_GameObject, (0,0,0), (0,0,0), KX_PolyProxy, (0,0))

	def setCollisionMargin(self, margin):
		"""Set the objects collision margin."""

	def sendMessage(self, subject, body="", to=""):
		"""Sends a message."""

	def reinstancePhysicsMesh(self, gameObject, meshObject, dupli):
		"""Updates the physics system with the changed mesh."""
		return bool()

	def replacePhysicsShape(self, gameObject):
		"""Replace the current physics shape."""

	def get(self, key, default=None):
		"""Return the value matching key, or the default value if its not found.
:return: The key value or a default."""

	def playAction(self, name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=None, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=None):
		"""Plays an action."""

	def stopAction(self, layer=0):
		"""Stop playing the action on the given layer."""

	def getActionFrame(self, layer=0):
		"""Gets the current frame of the action playing in the supplied layer."""
		return float()

	def getActionName(self, layer=0):
		"""Gets the name of the current action playing in the supplied layer."""
		return str()

	def setActionFrame(self, frame, layer=0):
		"""Set the current frame of the action playing in the supplied layer."""

	def isPlayingAction(self, layer=0):
		"""Checks to see if there is an action playing in the given layer."""
		return bool()

	def addDebugProperty(self, name, debug = True):
		"""Adds a single debug property to the debug list."""


class KX_CubeMap(CValue):
	"""Python API for realtime cube map textures."""

	def __init__(self):
		self.autoUpdate = bool()
		self.viewpointObject = KX_GameObject()
		self.enabled = bool()
		self.ignoreLayers = int()
		self.clipStart = float()
		self.clipEnd = float()
		self.lodDistanceFactor = float()

	def update(self):
		"""Request to update this cube map during the rendering stage. This function is effective only when autoUpdate is disabled."""


class BL_Texture(CValue):
	"""A texture object that contains attributes of a material texture."""

	def __init__(self):
		self.diffuseIntensity = float()
		self.diffuseFactor = float()
		self.alpha = float()
		self.specularIntensity = float()
		self.specularFactor = float()
		self.hardness = float()
		self.emit = float()
		self.mirror = float()
		self.normal = float()
		self.parallaxBump = float()
		self.parallaxStep = float()
		self.lodBias = float()
		self.bindCode = int()
		self.cubeMap = KX_CubeMap()
		self.ior = float()
		self.refractionRatio = float()
		self.uvOffset = mathutils.Vector()
		self.uvSize = mathutils.Vector()
		self.uvRotation = float()


class KX_BlenderMaterial(PyObjectPlus):
	"""This is the interface to materials in the game engine."""

	def __init__(self):
		self.shader = BL_Shader()
		self.blending = (0,0)
		self.alpha = float()
		self.hardness = int()
		self.emit = float()
		self.ambient = float()
		self.specularAlpha = float()
		self.specularIntensity = float()
		self.diffuseIntensity = float()
		self.specularColor = mathutils.Color()
		self.diffuseColor = mathutils.Color()
		self.textures = BL_Texture()

	def getShader(self):
		"""Returns the material’s shader."""
		return BL_Shader()

	def getTextureBindcode(self, textureslot):
		"""Returns the material’s texture OpenGL bind code/id/number/name."""
		return int()

	def setBlending(self, src, dest):
		"""Set the pixel color arithmetic functions."""


class KX_VertexProxy(SCA_IObject):
	"""A vertex holds position, UV, color and normal information."""

	def __init__(self):
		self.XYZ = mathutils.Vector()
		self.UV = mathutils.Vector()
		self.uvs = CListValue(mathutils.Vector)
		self.normal = mathutils.Vector()
		self.color = mathutils.Vector()
		self.colors = CListValue(mathutils.Vector)
		self.x = float()
		self.y = float()
		self.z = float()
		self.u = float()
		self.v = float()
		self.u2 = float()
		self.v2 = float()
		self.r = float()
		self.g = float()
		self.b = float()
		self.a = float()

	def getXYZ(self):
		"""Gets the position of this vertex."""
		return mathutils.Vector()

	def setXYZ(self, pos):
		"""Sets the position of this vertex."""

	def getUV(self):
		"""Gets the UV (texture) coordinates of this vertex."""
		return mathutils.Vector()

	def setUV(self, uv):
		"""Sets the UV (texture) coordinates of this vertex."""

	def getUV2(self):
		"""Gets the 2nd UV (texture) coordinates of this vertex."""
		return mathutils.Vector()

	def setUV2(self, uv, unit):
		"""Sets the 2nd UV (texture) coordinates of this vertex."""

	def getRGBA(self):
		"""Gets the color of this vertex."""
		return int()

	def setRGBA(self, col):
		"""Sets the color of this vertex."""

	def getNormal(self):
		"""Gets the normal vector of this vertex."""
		return mathutils.Vector()

	def setNormal(self, normal):
		"""Sets the normal vector of this vertex."""


class KX_PolyProxy(SCA_IObject):
	"""A polygon holds the index of the vertex forming the poylgon."""

	def __init__(self):
		self.material_name = str()
		self.material = KX_BlenderMaterial()
		self.texture_name = str()
		self.material_id = int()
		self.v1 = int()
		self.v2 = int()
		self.v3 = int()
		self.v4 = int()
		self.visible = int()
		self.collide = int()
		self.vertices = KX_VertexProxy()

	def getMaterialName(self):
		"""Returns the polygon material name with MA prefix"""
		return str()

	def getMaterial(self):
		return KX_BlenderMaterial()

	def getTextureName(self):
		return str()

	def getMaterialIndex(self):
		"""Returns the material bucket index of the polygon.
This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from MeshProxy."""
		return int()

	def getNumVertex(self):
		"""Returns the number of vertex of the polygon."""
		return int()

	def isVisible(self):
		"""Returns whether the polygon is visible or not"""
		return bool()

	def isCollider(self):
		"""Returns whether the polygon is receives collision or not"""
		return int()

	def getVertexIndex(self, vertex):
		"""Returns the mesh vertex index of a polygon vertex
This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from MeshProxy."""
		return int()

	def getMesh(self):
		"""Returns a mesh proxy"""
		return KX_MeshProxy()


class KX_MeshProxy(CValue):
	"""A mesh object."""

	def __init__(self):
		self.materials = CListValue(KX_BlenderMaterial)
		self.numPolygons = int()
		self.numMaterials = int()
		self.polygons = KX_PolyProxy()

	def getMaterialName(self, matid):
		"""Gets the name of the specified material."""
		return str()

	def getTextureName(self, matid):
		"""Gets the name of the specified material’s texture."""
		return str()

	def getVertexArrayLength(self, matid):
		"""Gets the length of the vertex array associated with the specified material."""
		return int()

	def getVertex(self, matid, index):
		"""Gets the specified vertex from the mesh object."""
		return KX_VertexProxy()

	def getPolygon(self, index):
		"""Gets the specified polygon from the mesh."""
		return KX_PolyProxy()

	def transform(self, matid, matrix):
		"""Transforms the vertices of a mesh."""

	def transformUV(self, matid, matrix, uv_index=-1, uv_index_from=-1):
		"""Transforms the vertices UV’s of a mesh."""

	def replaceMaterial(self, matid, material):
		"""Replace the material in slot matid by the material material."""


class KX_CharacterWrapper(PyObjectPlus):
	"""A wrapper to expose character physics options."""

	def __init__(self):
		self.onGround = bool()
		self.gravity = float()
		self.maxJumps = int()
		self.jumpCount = int()
		self.walkDirection = mathutils.Vector()

	def jump(self):
		"""The character jumps based on it’s jump speed."""


class KX_VehicleWrapper(PyObjectPlus):
	"""KX_VehicleWrapper"""

	def __init__(self):
		self.rayMask = int()

	def addWheel(self, wheel, attachPos, downDir, axleDir, suspensionRestLength, wheelRadius, hasSteering):
		"""Add a wheel to the vehicle"""

	def applyBraking(self, force, wheelIndex):
		"""Apply a braking force to the specified wheel"""

	def applyEngineForce(self, force, wheelIndex):
		"""Apply an engine force to the specified wheel"""

	def getConstraintId(self):
		"""Get the constraint ID"""
		return int()

	def getConstraintType(self):
		"""Returns the constraint type."""
		return int()

	def getNumWheels(self):
		"""Returns the number of wheels."""
		return int()

	def getWheelOrientationQuaternion(self, wheelIndex):
		"""Returns the wheel orientation as a quaternion."""
		return mathutils.Matrix()

	def getWheelPosition(self, wheelIndex):
		"""Returns the position of the specified wheel"""
		return [0,0,0]

	def getWheelRotation(self, wheelIndex):
		"""Returns the rotation of the specified wheel"""
		return float()

	def setRollInfluence(self, rollInfluece, wheelIndex):
		"""Set the specified wheel’s roll influence.
The higher the roll influence the more the vehicle will tend to roll over in corners."""

	def setSteeringValue(self, steering, wheelIndex):
		"""Set the specified wheel’s steering"""

	def setSuspensionCompression(self, compression, wheelIndex):
		"""Set the specified wheel’s compression"""

	def setSuspensionDamping(self, damping, wheelIndex):
		"""Set the specified wheel’s damping"""

	def setSuspensionStiffness(self, stiffness, wheelIndex):
		"""Set the specified wheel’s stiffness"""

	def setTyreFriction(self, friction, wheelIndex):
		"""Set the specified wheel’s tyre friction"""


class SCA_IController(SCA_ILogicBrick):
	"""Base class for all controller logic bricks."""

	def __init__(self):
		self.state = int()
		self.sensors = dict()
		self.actuators = dict()
		self.useHighPriority = bool()


class SCA_PythonController(SCA_IController):
	"""A Python controller uses a Python script to activate it’s actuators,
based on it’s sensors."""

	def __init__(self):
		self.owner = KX_GameObject()
		self.script = str()
		self.mode = int()

	def activate(self, actuator):
		"""Activates an actuator attached to this controller."""

	def deactivate(self, actuator):
		"""Deactivates an actuator attached to this controller."""


class KX_LightObject(KX_GameObject):
	"""A Light object."""

	def __init__(self):
		self.SPOT = int()
		self.SUN = int()
		self.NORMAL = int()
		self.HEMI = int()
		self.type = None
		self.energy = float()
		self.shadowClipStart = float()
		self.shadowClipEnd = float()
		self.shadowFrustumSize = float()
		self.shadowBindId = int()
		self.shadowMapType = int()
		self.shadowBias = float()
		self.shadowBleedBias = float()
		self.useShadow = bool()
		self.shadowColor = mathutils.Color()
		self.shadowMatrix = mathutils.Matrix()
		self.distance = float()
		self.color = [0,0,0]
		self.lin_attenuation = float()
		self.quad_attenuation = float()
		self.spotsize = float()
		self.spotblend = float()
		self.staticShadow = bool()

	def updateShadow(self):
		"""Set the shadow to be updated next frame if the lamp uses a static shadow, see staticShadow."""


class KX_Camera(KX_GameObject):
	"""A Camera object."""

	def __init__(self):
		self.INSIDE = int()
		self.INTERSECT = int()
		self.OUTSIDE = int()
		self.lens = float()
		self.lodDistanceFactor = float()
		self.fov = float()
		self.ortho_scale = float()
		self.near = float()
		self.far = float()
		self.shift_x = float()
		self.shift_y = float()
		self.perspective = bool()
		self.frustum_culling = bool()
		self.projection_matrix = mathutils.Matrix()
		self.modelview_matrix = mathutils.Matrix()
		self.camera_to_world = mathutils.Matrix()
		self.world_to_camera = mathutils.Matrix()
		self.useViewport = bool()

	def sphereInsideFrustum(self, centre, radius):
		"""Tests the given sphere against the view frustum."""
		return int()

	def boxInsideFrustum(self, box):
		"""Tests the given box against the view frustum."""

	def pointInsideFrustum(self, point):
		"""Tests the given point against the view frustum."""
		return bool()

	def getCameraToWorld(self):
		"""Returns the camera-to-world transform."""
		return mathutils.Matrix()

	def getWorldToCamera(self):
		"""Returns the world-to-camera transform."""
		return mathutils.Matrix()

	def setOnTop(self):
		"""Set this cameras viewport ontop of all other viewport."""

	def setViewport(self, left, bottom, right, top):
		"""Sets the region of this viewport on the screen in pixels."""

	def getScreenPosition(self, object):
		"""Gets the position of an object projected on screen space."""
		return [0,0]

	def getScreenVect(self, x, y):
		"""Gets the vector from the camera position in the screen coordinate direction."""
		return mathutils.Vector()

	def getScreenRay(self, x, y, dist=inf, property=None):
		"""Look towards a screen coordinate (x, y) and find first object hit within dist that matches prop.
The ray is similar to KX_GameObject->rayCastTo."""
		return KX_GameObject()


class KX_FontObject(KX_GameObject):
	"""A Font object."""

	def __init__(self):
		self.text = str()
		self.resolution = float()
		self.size = float()
		self.dimensions = mathutils.Vector()


class KX_WorldInfo(PyObjectPlus):
	"""A world object."""

	def __init__(self):
		self.KX_MIST_QUADRATIC = int()
		self.KX_MIST_LINEAR = int()
		self.KX_MIST_INV_QUADRATIC = int()
		self.mistEnable = bool()
		self.mistStart = float()
		self.mistDistance = float()
		self.mistIntensity = float()
		self.mistType = None
		self.mistColor = mathutils.Color()
		self.horizonColor = mathutils.Color()
		self.zenithColor = mathutils.Color()
		self.ambientColor = mathutils.Color()
		self.exposure = float()
		self.range = float()


class KX_2DFilterManager(PyObjectPlus):
	"""2D filter manager used to add, remove and find filters in a scene."""


	def addFilter(self, index, type, fragmentProgram):
		"""Add a filter to the pass index index, type type and fragment program if custom filter."""

	def removeFilter(self, index):
		"""Remove filter to the pass index index."""

	def getFilter(self, index):
		"""Return filter to the pass index index."""


class KX_Scene(PyObjectPlus):
	"""An active scene that gives access to objects, cameras, lights and scene attributes."""

	def __init__(self):
		self.name = str()
		self.objects = CListValue(KX_GameObject)
		self.objectsInactive = CListValue(KX_GameObject)
		self.lights = CListValue(KX_LightObject)
		self.cameras = CListValue(KX_Camera)
		self.texts = CListValue(KX_FontObject)
		self.active_camera = KX_Camera()
		self.world = KX_WorldInfo()
		self.filterManager = KX_2DFilterManager()
		self.suspended = bool()
		self.activity_culling = bool()
		self.activity_culling_radius = float()
		self.dbvt_culling = bool()
		self.pre_draw = list()
		self.post_draw = list()
		self.pre_draw_setup = list()
		self.gravity = mathutils.Vector()

	def addObject(self, object, reference, time=0.0):
		"""Adds an object to the scene like the Add Object Actuator would."""
		return KX_GameObject()

	def end(self):
		"""Removes the scene from the game."""

	def restart(self):
		"""Restarts the scene."""

	def replace(self, scene):
		"""Replaces this scene with another one."""
		return bool()

	def suspend(self):
		"""Suspends this scene."""

	def resume(self):
		"""Resume this scene."""

	def get(self, key, default=None):
		"""Return the value matching key, or the default value if its not found.
:return: The key value or a default."""

	def drawObstacleSimulation(self):
		"""Draw debug visualization of obstacle simulation."""

