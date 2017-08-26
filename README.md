__Welcome to UPBGE's Community Addon GitHub__

The Community Addon is a framework for UPBGE. It adds features and provides a new and easy to use hight level Python API. Most features can also by accessed visually from Blender GUI.

## Documentation:
* API Reference and Tutorials: [http://coredoc.royalwebhosting.net/](http://coredoc.royalwebhosting.net/)
* Blenderartists thread: [Here](https://blenderartists.org/forum/showthread.php?413239-UPBGE-s-Community-Addon)

_The documentation generator files are included in the repository. To build with Sphinx, check the folders readme._

## Features
* Premade components for movement, control and media playback. (Most are simply wrappers to functions of the Python API)
* Amazing yet simple keybinding: [See example](http://coredoc.royalwebhosting.net/api/event.html#key-bindings)
* Tweening capabilities (Sequencer): Wait, LinerInterpolation, etc.
* Premade 2D Filters (GLSL Shaders)
* UI Panel for selecting 2D Filters graphically and configuring them.
* Generic 2D Filter class for easy implementation of custom filters in Python.
* Media API for easy playback of music and sound effects.
* Save/Load utility fuctions.
* Launcher with configuration file (set BGE flags before starting Blender)
* Build system (Windows only, other platforms may be build manually), replaces "Save as Runtime Executable" addon.
* Dummy Python API (+UPBGE API) for code editor autocompletion.

_NOTE: The Python API that this addon provides is called BGECore._

__IMPORTANT: This library is a side project of mine and is not being currently developed. It's not recomended for production (neither UPBGE actually), doesn't include a test suit and lacks most common components that large game engines have. Nonetheless is useful and easy to modify. Feel free to extend it with your own code.__

### What this library is not
It's not a fork of BGE, I don't touch a single line of Blender's source code. It's not a networking library. It's not a system to avoid GPL licenses. It's not a system to improve logic bricks or visual programing.

## Install
* [Install Instructions](http://coredoc.royalwebhosting.net/index.html)
* Recomended: [First steps tutorial](http://coredoc.royalwebhosting.net/ui.html)
* Recomended: [Build System](http://coredoc.royalwebhosting.net/ui/game_project.html)

## Copyright
Robert Planas Jimenez (elmeunick9@gmail.com)
Licensed under GPL3.0
