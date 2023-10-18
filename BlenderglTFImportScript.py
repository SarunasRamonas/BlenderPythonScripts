import os
import bpy

def find_all_gltf_files_in_directory(directory):
    gltf_files = []
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".gltf"):
                gltf_files.append(os.path.join(root, filename))
    return gltf_files

def import_gltf_files(gltf_files):
    for gltf_file in gltf_files:
        # Import the GLTF file.
        bpy.ops.import_scene.gltf(filepath=gltf_file)


directory = r"C:\import"
directory = directory.replace("\\","/")

gltf_files = find_all_gltf_files_in_directory(directory)

import_gltf_files(gltf_files)
