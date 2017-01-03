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

	uniform variableName;
	uniform variableNameTwo;
	//More...
	
	const float tolerance = 0.6;
	//More...
	
	void main(void)
	{
		//More...
		gl_FragColor = vec4(1.0); //Or any other vec4 structure.
	}
	
Once you have the shader done, you must create the documentation and specify the initialization values. The documentation is writted for ReST for Sphinx. The name of the class must be the filename of the shader. The class attributes will define the uniforms. Attributes defined in ``__init__`` won't be taken as uniforms. You can create new methods to use with complex shaders. Example:

.. code-block:: python

	from filter2D import Filter2D

	class FilterName(Filter2D):
		"""
		A filter2D subclass.
		
		.. attribute:: variableName
			
			This does something.
			
		[...]
		"""
		
		variableName = 0.0
		variableNameTwo = 6.182
		
Additionally you can override the ``__define__`` method in order to use bge on the shader wrapper. Do not import the bge API outside this method, or else the UI Panel for custom shaders won't work properly. Uniforms defined inside this method won't appear in the UI Panel.


Trublesome
-----------------------------------------------
The following list contains known features that break on some computers:

* Using implicit conversion of types, like ``float x = 1.0; x /= 2;``. Instead use explicit conversion ``x = x / 2.0``.