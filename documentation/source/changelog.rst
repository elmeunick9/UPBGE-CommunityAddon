Change Log
==================

Version 0.2
-----------------
 * 170110 - Added KeyBind system, wich will be useful for components. Now you can change any component keys with it to any other key or function.
 * 170110 - Added "Invert on Backwards" and "Jump Ticks" arguments to the ThirdPerson component.
 * 170109 - Added fake Bloom and updated documentation.
 * 170109 - Now the media.Screen class will libload a Sreen automatically and make it invisible if no object is provided.
 * 170108 - Removed old fix on media.Screen about audio sync that wasn't working propery since it's now already fixed in the GE source. 
 * 170108 - Added "VideoTexture.Texture", "("bindCode", bindId)", and "(bgl.Buffer, sizex, sizey)" as possible new sampler2D uniforms.
 * 170107 - Added UI for selecting texture filepath for 2DFilters
 * 170107 - Added textures (internal and external) easy binding for 2DFilters.
 * 170107 - Added int as a valid type of uniform for automatic binding.
 * 170107 - Added events: "on_scene_added", "on_scene_removed" and "on_next_frame"
 * 170107 - Fixed bug with 2DFilters instanced from UI didn't load on overlay scenes.
 * 170105 - Added MotionBlur 2DFilter, but still needs some improvements.
 * 170105 - Added Matrix uniforms to the 2DFilter class. Now the only left is integer.
 * 170105 - Added control.TrackToNearest component and utils.getNearestObject function.
 * 170105 - Fixed bug on core.utils.getLocalDirectory()
 * 170105 - Added Export Game Project operator and functionality + new launcher (Windows Only).
 * 170105 - Fixed bug with New Game Project where "data.zip" wasn't being properly packed.
 * 170104 - Added operators for save As, and load packed.
 * 170103 - Added RadialBlur, LSD, GameBoyColor and ToonLine 2DFilters.
 * 170103 - Added images at the filters documentation.
 * 170103 - Added control.Follow component.