from .macro import *
from . import utils
import bpy
import bpy.props as prop

class ListItem(bpy.types.PropertyGroup):
	""" Group of properties representing an item in the list """

	name = prop.StringProperty(
		   name="Name",
		   description="A name for this item",
		   default="Untitled")
		   

class MY_UL_List(bpy.types.UIList):
	def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

		# We could write some code to decide which icon to use here...
		custom_icon = 'OBJECT_DATAMODE'

		# Make sure your code supports all 3 layout types
		if self.layout_type in {'DEFAULT', 'COMPACT'}:
			layout.label(item.name, icon = custom_icon)

		elif self.layout_type in {'GRID'}:
			layout.alignment = 'CENTER'
			layout.label("", icon = custom_icon)


class LIST_OT_NewItem(bpy.types.Operator):
	""" Add a new item to the list """

	bl_idname = "my_list.new_item"
	bl_label = "Add a new item"
	
	
	filterName = bpy.props.StringProperty()

	def execute(self, context):
		if self.filterName == "": return{'CANCELLED'}
		
		p=context.scene.my_list.add()
		context.scene.list_index = len(context.scene.my_list)-1
		p.name = self.filterName
		
		return{'FINISHED'}


class LIST_OT_DeleteItem(bpy.types.Operator):
	""" Delete the selected item from the list """

	bl_idname = "my_list.delete_item"
	bl_label = "Deletes an item"

	@classmethod
	def poll(self, context):
		""" Enable if there's something in the list """
		return len(context.scene.my_list) > 0

	def execute(self, context):
		list = context.scene.my_list
		index = context.scene.list_index

		utils.checkProjectFile()
		try:
			sf = utils.project_data["bge-project"]["settings"]["filter2D"][bpy.context.scene.name]
	
			for i in range(index, len(list)-1): sf[str(i)] = sf[str(i+1)]
			del sf[str(len(list)-1)]
			
			utils.saveProjectFile()
		except KeyError: pass
		
		list.remove(index)

		if index > 0:
			index = index - 1

		return{'FINISHED'}

import inspect
def getAttrFromPython(path, classname):
	with open(path) as f: code = f.read()
	
	code = code.replace('import filter2D', '#')
	code = code.replace('from filter2D', '#')
	
	code = "class Filter2D: pass\n" + code
	
	code = compile(code, path, 'exec')
	myglob = dict()
	exec(code, dict(), myglob)
	
	attr = dict()
	_class = myglob[classname]
	for key, value in _class.__dict__.items():
		if key.startswith('__'): continue
		if inspect.ismethod(getattr(_class, key)): continue
		if inspect.isfunction(getattr(_class, key)): continue
		
		attr[key]=value
	
	return attr
		
		
class PT_FiltersList(bpy.types.Panel):
	"""Demo panel for UI list Tutorial"""
	
	bl_label = "Custom 2D Filters"
	bl_idname = "SCENE_PT_CUSTOM2DFILTERS"
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "render_layer"

	@classmethod
	def poll(cls, context):
		scene = context.scene
		return scene and (scene.render.engine == "BLENDER_GAME") and utils.project_data != None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
	
		layout = self.layout
		scene = context.scene
		
		row = layout.row(align=True)
		row.prop(scene, "aas")
		row.operator("my_list.new_item", text="", icon='ZOOMIN').filterName = scene.aas

		
		row = layout.row()
		row.template_list("MY_UL_List", "Filter2DList", scene, "my_list", scene, "list_index" )

		row = layout.row() 
		row.operator('my_list.delete_item', text='REMOVE')		 	 
			
		if scene.list_index >= 0 and len(scene.my_list) > 0:
			if scene.list_index >= len(scene.my_list): scene.list_index = 0
			item = scene.my_list[scene.list_index]
			name = item.name
			row = layout.row()
			
			path = os.path.dirname(bpy.data.filepath) + os.sep + "core" + os.sep + "glsl" + os.sep + name + ".py"
			uniforms = getAttrFromPython(path, name)
			
			def getListVal(key): return str(getattr(bpy.context.scene.my_list[scene.list_index], key))
			
			functx = "glsl." + name + "("
			for key, values in uniforms.items():
				if type(values) in [list, tuple]:
					row = layout.row()
					col = row.column(align=True)
					if key+'0' in ListItem.__dict__: functx += key + "=("
					for i, value in enumerate(values):
						if not key+str(i) in ListItem.__dict__:
							setattr(ListItem, key+str(i), bpy.props.FloatProperty(name=key, default=value))
						else: functx += getListVal(key + str(i)) + ", "
						col.prop(item, key+str(i))
					if key+'0' in ListItem.__dict__: functx = functx[:-2] + ")"
							
				else:
					if not key in ListItem.__dict__: setattr(ListItem, key, bpy.props.FloatProperty(name=key, default=values))
					else:
						functx += key + "=" + getListVal(key)
					row = layout.row()
					row.prop(item, key)
				
				functx += ", "
			
			if functx[-2:] == ", ": functx = functx[:-2] + ")"
			else: functx += ")"
			if "=" in functx or "()" in functx:
				if not utils.checkProjectFile(): return
				
				functx = "bge.logic.globalDict['__reserved__']['filter2D']['" + scene.name + "'][" +  str(scene.list_index) + ']=' + functx
				
				settings = utils.project_data["bge-project"]["settings"]
				if not "filter2D" in settings: settings["filter2D"] = {}
				if not scene.name in settings["filter2D"]: settings["filter2D"][scene.name] = {}
				settings["filter2D"][scene.name][str(scene.list_index)] = functx
				utils.saveProjectFile()
				
			
import os, bpy

def populateFilterSelector(self, context):
	path = os.path.dirname(bpy.data.filepath) + os.sep + "core" + os.sep + "glsl" + os.sep
	list = []
	for x in os.listdir(path):
		if not x.endswith(".filter2D"): continue
		name = os.path.basename(x)[:-9]
		if os.path.isfile(path + x) and os.path.isfile(path + x[:-9] + ".py"):
			list.append((name, name, path + x))
	
	return list
	
def register():
	bpy.utils.register_class(ListItem)
	bpy.utils.register_class(MY_UL_List)
	bpy.utils.register_class(LIST_OT_NewItem)
	bpy.utils.register_class(LIST_OT_DeleteItem)
	bpy.utils.register_class(PT_FiltersList)

	bpy.types.Scene.my_list = prop.CollectionProperty(type = ListItem)
	bpy.types.Scene.list_index = prop.IntProperty(name = "Index for my_list", default = 0)
	bpy.types.Scene.aas=bpy.props.EnumProperty(items=populateFilterSelector, name="2DFilter")
	
	
def unregister():
	del bpy.types.Scene.my_list
	del bpy.types.Scene.list_index
	del bpy.types.Scene.aas
	
	bpy.utils.unregister_class(ListItem)
	bpy.utils.unregister_class(MY_UL_List)
	bpy.utils.unregister_class(LIST_OT_NewItem)
	bpy.utils.unregister_class(LIST_OT_DeleteItem)
	bpy.utils.unregister_class(PT_FiltersList)
