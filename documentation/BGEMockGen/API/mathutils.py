
class Color:
	"""This object gives access to Colors in Blender."""

	def __init__(self, rgb=None):
		self.b = float()
		self.g = float()
		self.h = float()
		self.hsv = float()
		self.is_frozen = bool()
		self.is_wrapped = bool()
		self.owner = None
		self.r = float()
		self.s = float()
		self.v = float()


class Euler:
	"""This object gives access to Eulers in Blender."""

	def __init__(self, angles=None, order='XYZ'):
		self.is_frozen = bool()
		self.is_wrapped = bool()
		self.order = str()
		self.owner = None
		self.x = float()
		self.y = float()
		self.z = float()

	def make_compatible(self, other):
		"""Make this euler compatible with another,
so interpolating between them works as intended."""

	def rotate(self, other):
		"""Rotates the euler by another mathutils value."""

	def rotate_axis(self, axis, angle):
		"""Rotates the euler a certain amount and returning a unique euler rotation
(no 720 degree pitches)."""

	def to_matrix(self):
		"""Return a matrix representation of the euler."""
		return Matrix()

	def to_quaternion(self):
		"""Return a quaternion representation of the euler."""
		return Quaternion()

	def zero(self):
		"""Set all values to zero."""


class Matrix:
	"""This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4."""

	def __init__(self, rows=None):
		self.col = self
		self.is_frozen = bool()
		self.is_negative = bool()
		self.is_orthogonal = bool()
		self.is_orthogonal_axis_vectors = bool()
		self.is_wrapped = bool()
		self.median_scale = float()
		self.owner = None
		self.row = self
		self.translation = Vector()

	def adjugate(self):
		"""Set the matrix to its adjugate."""

	def adjugated(self):
		"""Return an adjugated copy of the matrix."""
		return self

	def copy(self):
		"""Returns a copy of this matrix."""
		return self

	def decompose(self):
		"""Return the location, rotation and scale components of this matrix."""
		return Quaternion()

	def determinant(self):
		"""Return the determinant of a matrix."""
		return float()

	def identity(self):
		"""Set the matrix to the identity matrix."""

	def invert(self, fallback=None):
		"""Set the matrix to its inverse."""

	def invert_safe(self):
		"""Set the matrix to its inverse, will never error.
If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
If tweaked matrix is still degenerated, set to the identity matrix instead."""

	def inverted(self, fallback=None):
		"""Return an inverted copy of the matrix."""
		return self

	def inverted_safe(self):
		"""Return an inverted copy of the matrix, will never error.
If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
If tweaked matrix is still degenerated, return the identity matrix instead."""
		return self

	def normalize(self):
		"""Normalize each of the matrix columns."""

	def normalized(self):
		"""Return a column normalized matrix"""
		return self

	def resize_4x4(self):
		"""Resize the matrix to 4x4."""

	def rotate(self, other):
		"""Rotates the matrix by another mathutils value."""

	def to_3x3(self):
		"""Return a 3x3 copy of this matrix."""
		return self

	def to_4x4(self):
		"""Return a 4x4 copy of this matrix."""
		return self

	def to_euler(self, order, euler_compat):
		"""Return an Euler representation of the rotation matrix
(3x3 or 4x4 matrix only)."""
		return Euler()

	def to_quaternion(self):
		"""Return a quaternion representation of the rotation matrix."""
		return Quaternion()

	def to_scale(self):
		"""Return the scale part of a 3x3 or 4x4 matrix."""
		return Vector()

	def to_translation(self):
		"""Return the translation part of a 4 row matrix."""
		return Vector()

	def transpose(self):
		"""Set the matrix to its transpose."""

	def transposed(self):
		"""Return a new, transposed matrix."""
		return self

	def zero(self):
		"""Set all the matrix values to zero."""
		return self


class Quaternion:
	"""This object gives access to Quaternions in Blender."""

	def __init__(self, seq=None, angle=None):
		self.angle = float()
		self.axis = Vector()
		self.is_frozen = bool()
		self.is_wrapped = bool()
		self.magnitude = float()
		self.owner = None
		self.w = float()
		self.x = float()
		self.y = float()
		self.z = float()

	def cross(self, other):
		"""Return the cross product of this quaternion and another."""
		return self

	def dot(self, other):
		"""Return the dot product of this quaternion and another."""
		return self

	def rotate(self, other):
		"""Rotates the quaternion by another mathutils value."""

	def to_axis_angle(self):
		"""Return the axis, angle representation of the quaternion."""
		return (Vector(), float())

	def to_euler(self, order, euler_compat):
		"""Return Euler representation of the quaternion."""
		return Euler()

	def to_exponential_map(self):
		"""Return the exponential map representation of the quaternion."""
		return Vector()

	def to_matrix(self):
		"""Return a matrix representation of the quaternion."""
		return Matrix()


class Vector:
	"""This object gives access to Vectors in Blender."""

	def __init__(self, seq=None):
		self.is_frozen = bool()
		self.is_wrapped = bool()
		self.length = float()
		self.length_squared = float()
		self.magnitude = float()
		self.owner = None
		self.w = float()
		self.ww = None
		self.www = None
		self.wwww = None
		self.wwwx = None
		self.wwwy = None
		self.wwwz = None
		self.wwx = None
		self.wwxw = None
		self.wwxx = None
		self.wwxy = None
		self.wwxz = None
		self.wwy = None
		self.wwyw = None
		self.wwyx = None
		self.wwyy = None
		self.wwyz = None
		self.wwz = None
		self.wwzw = None
		self.wwzx = None
		self.wwzy = None
		self.wwzz = None
		self.wx = None
		self.wxw = None
		self.wxww = None
		self.wxwx = None
		self.wxwy = None
		self.wxwz = None
		self.wxx = None
		self.wxxw = None
		self.wxxx = None
		self.wxxy = None
		self.wxxz = None
		self.wxy = None
		self.wxyw = None
		self.wxyx = None
		self.wxyy = None
		self.wxyz = None
		self.wxz = None
		self.wxzw = None
		self.wxzx = None
		self.wxzy = None
		self.wxzz = None
		self.wy = None
		self.wyw = None
		self.wyww = None
		self.wywx = None
		self.wywy = None
		self.wywz = None
		self.wyx = None
		self.wyxw = None
		self.wyxx = None
		self.wyxy = None
		self.wyxz = None
		self.wyy = None
		self.wyyw = None
		self.wyyx = None
		self.wyyy = None
		self.wyyz = None
		self.wyz = None
		self.wyzw = None
		self.wyzx = None
		self.wyzy = None
		self.wyzz = None
		self.wz = None
		self.wzw = None
		self.wzww = None
		self.wzwx = None
		self.wzwy = None
		self.wzwz = None
		self.wzx = None
		self.wzxw = None
		self.wzxx = None
		self.wzxy = None
		self.wzxz = None
		self.wzy = None
		self.wzyw = None
		self.wzyx = None
		self.wzyy = None
		self.wzyz = None
		self.wzz = None
		self.wzzw = None
		self.wzzx = None
		self.wzzy = None
		self.wzzz = None
		self.x = float()
		self.xw = None
		self.xww = None
		self.xwww = None
		self.xwwx = None
		self.xwwy = None
		self.xwwz = None
		self.xwx = None
		self.xwxw = None
		self.xwxx = None
		self.xwxy = None
		self.xwxz = None
		self.xwy = None
		self.xwyw = None
		self.xwyx = None
		self.xwyy = None
		self.xwyz = None
		self.xwz = None
		self.xwzw = None
		self.xwzx = None
		self.xwzy = None
		self.xwzz = None
		self.xx = None
		self.xxw = None
		self.xxww = None
		self.xxwx = None
		self.xxwy = None
		self.xxwz = None
		self.xxx = None
		self.xxxw = None
		self.xxxx = None
		self.xxxy = None
		self.xxxz = None
		self.xxy = None
		self.xxyw = None
		self.xxyx = None
		self.xxyy = None
		self.xxyz = None
		self.xxz = None
		self.xxzw = None
		self.xxzx = None
		self.xxzy = None
		self.xxzz = None
		self.xy = None
		self.xyw = None
		self.xyww = None
		self.xywx = None
		self.xywy = None
		self.xywz = None
		self.xyx = None
		self.xyxw = None
		self.xyxx = None
		self.xyxy = None
		self.xyxz = None
		self.xyy = None
		self.xyyw = None
		self.xyyx = None
		self.xyyy = None
		self.xyyz = None
		self.xyz = None
		self.xyzw = None
		self.xyzx = None
		self.xyzy = None
		self.xyzz = None
		self.xz = None
		self.xzw = None
		self.xzww = None
		self.xzwx = None
		self.xzwy = None
		self.xzwz = None
		self.xzx = None
		self.xzxw = None
		self.xzxx = None
		self.xzxy = None
		self.xzxz = None
		self.xzy = None
		self.xzyw = None
		self.xzyx = None
		self.xzyy = None
		self.xzyz = None
		self.xzz = None
		self.xzzw = None
		self.xzzx = None
		self.xzzy = None
		self.xzzz = None
		self.y = float()
		self.yw = None
		self.yww = None
		self.ywww = None
		self.ywwx = None
		self.ywwy = None
		self.ywwz = None
		self.ywx = None
		self.ywxw = None
		self.ywxx = None
		self.ywxy = None
		self.ywxz = None
		self.ywy = None
		self.ywyw = None
		self.ywyx = None
		self.ywyy = None
		self.ywyz = None
		self.ywz = None
		self.ywzw = None
		self.ywzx = None
		self.ywzy = None
		self.ywzz = None
		self.yx = None
		self.yxw = None
		self.yxww = None
		self.yxwx = None
		self.yxwy = None
		self.yxwz = None
		self.yxx = None
		self.yxxw = None
		self.yxxx = None
		self.yxxy = None
		self.yxxz = None
		self.yxy = None
		self.yxyw = None
		self.yxyx = None
		self.yxyy = None
		self.yxyz = None
		self.yxz = None
		self.yxzw = None
		self.yxzx = None
		self.yxzy = None
		self.yxzz = None
		self.yy = None
		self.yyw = None
		self.yyww = None
		self.yywx = None
		self.yywy = None
		self.yywz = None
		self.yyx = None
		self.yyxw = None
		self.yyxx = None
		self.yyxy = None
		self.yyxz = None
		self.yyy = None
		self.yyyw = None
		self.yyyx = None
		self.yyyy = None
		self.yyyz = None
		self.yyz = None
		self.yyzw = None
		self.yyzx = None
		self.yyzy = None
		self.yyzz = None
		self.yz = None
		self.yzw = None
		self.yzww = None
		self.yzwx = None
		self.yzwy = None
		self.yzwz = None
		self.yzx = None
		self.yzxw = None
		self.yzxx = None
		self.yzxy = None
		self.yzxz = None
		self.yzy = None
		self.yzyw = None
		self.yzyx = None
		self.yzyy = None
		self.yzyz = None
		self.yzz = None
		self.yzzw = None
		self.yzzx = None
		self.yzzy = None
		self.yzzz = None
		self.z = float()
		self.zw = None
		self.zww = None
		self.zwww = None
		self.zwwx = None
		self.zwwy = None
		self.zwwz = None
		self.zwx = None
		self.zwxw = None
		self.zwxx = None
		self.zwxy = None
		self.zwxz = None
		self.zwy = None
		self.zwyw = None
		self.zwyx = None
		self.zwyy = None
		self.zwyz = None
		self.zwz = None
		self.zwzw = None
		self.zwzx = None
		self.zwzy = None
		self.zwzz = None
		self.zx = None
		self.zxw = None
		self.zxww = None
		self.zxwx = None
		self.zxwy = None
		self.zxwz = None
		self.zxx = None
		self.zxxw = None
		self.zxxx = None
		self.zxxy = None
		self.zxxz = None
		self.zxy = None
		self.zxyw = None
		self.zxyx = None
		self.zxyy = None
		self.zxyz = None
		self.zxz = None
		self.zxzw = None
		self.zxzx = None
		self.zxzy = None
		self.zxzz = None
		self.zy = None
		self.zyw = None
		self.zyww = None
		self.zywx = None
		self.zywy = None
		self.zywz = None
		self.zyx = None
		self.zyxw = None
		self.zyxx = None
		self.zyxy = None
		self.zyxz = None
		self.zyy = None
		self.zyyw = None
		self.zyyx = None
		self.zyyy = None
		self.zyyz = None
		self.zyz = None
		self.zyzw = None
		self.zyzx = None
		self.zyzy = None
		self.zyzz = None
		self.zz = None
		self.zzw = None
		self.zzww = None
		self.zzwx = None
		self.zzwy = None
		self.zzwz = None
		self.zzx = None
		self.zzxw = None
		self.zzxx = None
		self.zzxy = None
		self.zzxz = None
		self.zzy = None
		self.zzyw = None
		self.zzyx = None
		self.zzyy = None
		self.zzyz = None
		self.zzz = None
		self.zzzw = None
		self.zzzx = None
		self.zzzy = None
		self.zzzz = None

	def cross(self, other):
		"""Return the cross product of this vector and another."""
		return Vector()

	def dot(self, other):
		"""Return the dot product of this vector and another."""
		return self

	def negate(self):
		"""Set all values to their negative."""

	def normalize(self):
		"""Normalize the vector, making the length of the vector always 1.0."""

	def normalized(self):
		"""Return a new, normalized vector."""
		return self

	def orthogonal(self):
		"""Return a perpendicular vector."""
		return self

	def reflect(self, mirror):
		"""Return the reflection vector from the mirror argument."""
		return self

	def resize(self, size=3):
		"""Resize the vector to have size number of elements."""

	def resize_2d(self):
		"""Resize the vector to 2D  (x, y)."""

	def resize_3d(self):
		"""Resize the vector to 3D  (x, y, z)."""

	def resize_4d(self):
		"""Resize the vector to 4D (x, y, z, w)."""

	def resized(self, size=3):
		"""Return a resized copy of the vector with size number of elements."""
		return self

	def to_2d(self):
		"""Return a 2d copy of the vector."""
		return self

	def to_3d(self):
		"""Return a 3d copy of the vector."""
		return self

	def to_4d(self):
		"""Return a 4d copy of the vector."""
		return self

	def to_track_quat(self, track, up):
		"""Return a quaternion rotation from the vector and the track and up axis."""
		return Quaternion()

	def to_tuple(self, precision=-1):
		"""Return this vector as a tuple with."""
		return tuple()

	def zero(self):
		"""Set all values to zero."""

