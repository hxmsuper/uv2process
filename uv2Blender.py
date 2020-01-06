import sys
import os  
import os.path
import string
workPath = os.getcwd()
blenderPath =  'C:/blender-2.80-windows64/blender.exe'
print(workPath)  
# Import FBX
for parent, dirnames, filenames in os.walk(workPath): 
    for filename in filenames:
        if(filename.find('.fbx')>0): 
            print(filename.replace('.fbx',''))
            filename = filename.replace('.fbx','') 
            os.system('RunWarp.bat '+workPath+'/'+'"'+filename+'"')
            