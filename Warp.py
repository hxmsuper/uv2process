import bpy
from random import random 
from math import radians
import sys
import os  
import os.path
import string
workPath = os.getcwd() 
print(workPath) 
context = bpy.context
scene = context.scene
# Import FBX
filename = ''
print(len(sys.argv))
if len(sys.argv)>3: 
        filename = sys.argv[4]
        print('filename:'+filename)
else:
    filename = 'C:/Users/2990wx/Documents/GitHub/uv2process/SM_Bld_Cabin_01'
bpy.ops.import_scene.fbx( filepath = filename+'.fbx' )

print(filename) 
 
objects = bpy.context.scene.objects 
for obj in objects : 
    if obj.type == 'MESH':   
        context.view_layer.objects.active = obj 
        obj.select_set(state=True)
        mesh = obj.data  
        print('start----------------------'+obj.name)
        if len(mesh.uv_layers) < 2:
            mesh.uv_layers.new(name='lm')
            lm = mesh.uv_layers.get('lm')
            bpy.ops.object.editmode_toggle()
            lm.active = True 
            mesh.uv_layers[1].active = True 
            bpy.ops.uv.lightmap_pack()
            print('end----------------------'+"lightmap pack")
            bpy.ops.object.editmode_toggle() 
print('start to export')
#bpy.ops.export_scene.fbx(filepath=(workPath+'/'+filename+".fbx"), axis_forward='-Z', axis_up='Y')
bpy.ops.export_scene.fbx(filepath=(workPath+'/'+"tttt.fbx"), axis_forward='-Z', axis_up='Y')
print("export success")   
 