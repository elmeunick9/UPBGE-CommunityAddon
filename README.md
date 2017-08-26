__Welcome to UPBGE's Community Addon GitHub__

The Community Addon is a framework for UPBGE. It adds features and provides a new and easy to use hight level Python API. Most features can also by accessed visually from Blender GUI.

## Documentation:
* API Reference and Tutorials: [http://coredoc.royalwebhosting.net/](http://coredoc.royalwebhosting.net/)
* Blenderartists thread: [Here](https://blenderartists.org/forum/showthread.php?413239-UPBGE-s-Community-Addon)

_The documentation generator files are included in the repository. To build with Sphinx, check the folders readme._

## Features
* Ready to use components.
* Amazing yet simple keybinding: [See example](http://coredoc.royalwebhosting.net/api/event.html#key-bindings)
* Tweening capabilities (Sequencer)
* Premade 2D Filters (GLSL Shaders): [See green-screen filter demo video](https://youtu.be/iiNVnp1Bo2c), with Shia LaBeouf. DO IT!
  * UI Panel for 2D Filters.
  * Generic 2D Filter class.
* Media API for easy playback of music and sound effects.
* Save/Load utility fuctions.
* Build system (Windows only, other platforms may be build manually)
  * Launcher with configuration file. _An external program made in C++_
* Dummy Python API (+UPBGE API) for code editor autocompletion.
  * Includes online documentation Scraper!

_NOTE: The Python API that this addon provides is called BGECore._

__IMPORTANT: This library is a side project of mine and is not being currently developed. It's not recomended for production (neither UPBGE actually), doesn't include a test suit and lacks most common components that large game engines have. Nonetheless is useful and easy to modify. Feel free to extend it with your own code.__

### What this library is not
It's not a fork of BGE, I don't touch a single line of Blender's source code. It's not a networking library. It's not a system to avoid GPL licenses. It's not a system to improve logic bricks or visual programing.

## Install
* [Install Instructions](http://coredoc.royalwebhosting.net/index.html)
* Recomended: [First steps tutorial](http://coredoc.royalwebhosting.net/ui.html)
* Recomended: [Build System](http://coredoc.royalwebhosting.net/ui/game_project.html)

## For developers and hackers
Feel free to join.

- The source code of the addon and the UI Panels is at: `addon/community/`
- The source code of the BGECore Python API is at: `project/core/`
  - The components at: `project/core/com/`
  - The 2DFilters at: `project/core/glsl/`
- You can execute `make` on the main directory to generate the addon.
- Consider adding make as a hook for git commits.

## Copyright
Robert Planas Jimenez (elmeunick9@gmail.com)
Licensed under GPL3.0
