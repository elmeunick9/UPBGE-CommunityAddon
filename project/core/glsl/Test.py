from filter2D import Filter2D
from bgl import *

class Test(Filter2D):

	def __define__(self):
		Test.iChannel0 = self.owner.scene.objects["Plane.001"].meshes[0].materials[0].textures[0]
		
	var = 10
	#iChannel0 = self.owner.scene.objects["Plane.001"].meshes[0].materials[0].textures[0]