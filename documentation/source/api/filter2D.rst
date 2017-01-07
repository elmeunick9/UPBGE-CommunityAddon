.. _filter2D:

Filters 2D - GLSL Shaders
=================================
Filters are GLSL shaders, a post-render phase where the image is edited to mod it in any way. Here you can find a list of the default BGECore 2D Filters and a tutorial into how to make your own GLSL shaders.

.. note:: This module is standalone and can be used outside the Core Framework by simple coping the ``core/glsl`` folder in the main game `.blend` directory.

Standard Shaders
-----------------------------------
Standard shaders can be used directly creatig an instance of a 2DFilter subclass. A shortcut to use them is the namescpace ``core.utils.filter2d``. Example:



.. code-block:: python

	from core import behavior, utils

	class EndOfTheWorld(behavior.Scene):
		def init(self):
			self.vignetting = utils.filter2D.Vignetting(colorR = 1.0)
			[...]
		
		def onKeyRelease(self, keys):
			if key.E in keys: self.vignetting.colorR = 0

Shaders initialized from the UI can be accesed in python with the following path: ``bge.logic.globalDict["__reserved__"]["filter2D"][SceneName][Index]``.

.. automodule:: core.glsl
	:members:
	
.. .. Debug



Installing or creating custom shaders
-----------------------------------------------
The `core` API uses the directory ``data/core/glsl`` for GLSL shaders. Such shaders must use the extension **.filter2D** when designed to be used as filters. If you have the source code of a shader, moving it there and creating a 2DFilter subclass should be enough to make it work, however shaders must be BGE complaint so you may need a little understanding of GLSL before you can use third party shaders not designed specifically for Blender.

The shaders are coded in GLSL, a language very similar to C that is compiled by BGE at runtime (when loading the shader). Depending on the version of Blender you're using you must guarantee that your shader can work with a min version of OpenGL.

When porting a third party shader it's important to look at the following things:

* It must be a fragment shader, meaning that in the shader at some point the variable **gl_FragColor** is used.
* It should have a **sampler2D uniform**, you need to rename it to *bgl_RenderedTexture* to make it work in BGE.
* It must have a **main** method.
* Build-in types that are predefined macros or constants can be converted to uniforms if you want to modify them in realtime.

The following template can be used (FilterName.filter2D):

.. code-block:: c

	uniform sampler2D bgl_RenderedTexture;
	
	unifrom sampler2D myTexture;
	uniform int myInteger;
	uniform float myFloat;
	uniform vec3 myVector;
	uniform mat4 myMatrix;

	//Commonly used
	uniform float iTime;
	uniform vec2 iResolution;
	
	//Constants
	const float tolerance = 0.6;
	//...
	
	void main(void)
	{
		//More...
		gl_FragColor = vec4(1.0); //Or any other vec4 structure.
	}
	
Once you have the shader done, you must create the documentation and specify the initialization values. The documentation is writted for ReST for Sphinx. The name of the class must be the filename of the shader. The class attributes will define the uniforms. You can create new methods to use with complex shaders. Example:

.. code-block:: python

	from filter2D import Filter2D
	import time

	class FilterName(Filter2D):
		"""
		A filter2D subclass.
		
		.. attribute:: myInteger
			
			This does something.
			
		[...]
		"""
		
		def __define__(self):
			from bge import render
			FilterName.iResolution = [render.getWindowWidth(), render.getWindowHeight()]
			FilterName.iTime = time.time()
			
		def load(self):
			super().load()
			self.scene.pre_draw.append(self.update)
		
		def unload(self):
			self.scene.pre_draw.remove(self.update)
			super.unload()
			
		def update():
			self.iTime = time.time()
		
		#You can also use textures stored in a material, but use the __define__ method.
		myTexture = "cool_cat.jpg" 
		
		myInteger = 8
		myFloat = 6.182
		myVector = [10.8, 2.0, 89]
		myMatrix = [[ 0, 1, 2, 3],
			    [ 4, 5, 6, 7],
			    [ 8, 9,10,11],
			    [12,13,14,15]]
		[...]
		
Additionally you can override the ``__define__`` method in order to use BGE on the shader wrapper. Do not import the BGE API at the module level, or else the UI Panel for custom shaders won't work properly. Uniforms defined inside this method won't appear in the UI Panel.

Once an uniform is defined as a class method, in order to be modified on real-time it has to be accesed as an object attribute.





Trublesome
-----------------------------------------------
The following list contains known features that break on some computers:

* Using implicit conversion of types, like ``float x = 1.0; x /= 2;``. Instead use explicit conversion ``x = x / 2.0``.

If you get an "Invalid uniform value: UniformName." message, most probably it's becouse you have an uniform that are not using in your shader (even if declared).