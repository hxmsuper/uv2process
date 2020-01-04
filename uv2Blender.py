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
for parent, dirnames, filenames in os.walk(workPath): 
    for filename in filenames:
        if(filename.find('.fbx')>0):
            bpy.ops.import_scene.fbx( filepath = workPath+'/'+filename )
            objects = bpy.context.scene.objects
            print("开始执行文件:"+filename)
            for obj in objects : 
                if obj.type == 'MESH': 
                    context.view_layer.objects.active = obj 
                    obj.select_set(state=True)
                    print(obj)
                    mesh = obj.data  
                    if len(mesh.uv_layers) < 2:
                        lm = mesh.uv_layers.new(name='lm')
                        lm.active = True 
                        bpy.ops.object.editmode_toggle()
                        bpy.ops.uv.smart_project(angle_limit=radians(66),island_margin = 0.02)
                        bpy.ops.object.editmode_toggle() 
            bpy.ops.export_scene.fbx(filepath=(workPath+'\done.fbx'), axis_forward='-Z', axis_up='Y')
            print("执行完毕，已经导出")
            for obj in objects : 
                bpy.ops.object.delete(obj)