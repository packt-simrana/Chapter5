bl_info = {
    "name": "A Very Simple Panel",
    "author": "John Doe",
    "version": (1, 0),
    "blender": (3, 2, 0),
    "description": "Just show up a panel in the UI",
    "category": "Learning",
}

import bpy
from bpy.utils import previews
import os
# global variable for icon storage
custom_icons = None

class OBJECT_PT_very_simple(bpy.types.Panel):
    """Creates a Panel in the object context of the
    properties editor"""
    
    bl_label = "A Very Simple Panel"
    bl_idname = "VERYSIMPLE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'object'

    def draw(self, context):
        layout = self.layout
        layout.label(text="A Very Simple Label",
                     icon='INFO')
        layout.label(text="Isn't it great?", 
                     icon='QUESTION')
        layout.label(text="Smile", icon_value=custom_icons['smile_face'].icon_id)


        pass

def load_custom_icons():
        """Load icon from the add-on folder"""
        Addon_path = os.path.dirname(__file__)
        img_file = os.path.join(Addon_path, "icon_smile_64.png")
        global custom_icons
        custom_icons = previews.new()
        custom_icons.load("smile_face",img_file, 'IMAGE')

def remove_custom_icons():
        """Clear Icons loaded from file"""
        global custom_icons
        bpy.utils.previews.remove(custom_icons)

def register():
    load_custom_icons()
    bpy.utils.register_class(OBJECT_PT_very_simple)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_very_simple)
    remove_custom_icons()
