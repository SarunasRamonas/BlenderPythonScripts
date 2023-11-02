import os
import bpy


# Define a panel class
class MultipleGLTFImporterPanel(bpy.types.Panel):
    bl_label = "Multiple GLTF Importer"
    bl_idname = "PT_MultipleGLTFImporterPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    # Define properties for the directory selector
    bpy.types.Scene.my_directory_path = bpy.props.StringProperty(
        name="Directory Path",
        description="Select a directory",
        subtype='DIR_PATH',
        default="",
    )

    # Define the content of the panel
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Add a directory selector
        layout.prop(scene, "my_directory_path")

        # Add the import button to the panel
        layout.operator("my_operator.import_button")

# Define an operator class for the import button
class ImportButton(bpy.types.Operator):
    bl_idname = "my_operator.import_button"
    bl_label = "Import GLTF Files"

    def execute(self, context):
        # Access the directory path property
        directory_path = context.scene.my_directory_path

        # Find all GLTF files in the directory
        gltf_files = find_all_gltf_files_in_directory(directory_path)

        # Import the GLTF files
        import_gltf_files(gltf_files)

        return {'FINISHED'}

# Define a function to find all GLTF files in a directory
def find_all_gltf_files_in_directory(directory):
    gltf_files = []
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".gltf"):
                gltf_files.append(os.path.join(root, filename))
    return gltf_files

# Define a function to import GLTF files
def import_gltf_files(gltf_files):
    for gltf_file in gltf_files:
        # Import the GLTF file.
        bpy.ops.import_scene.gltf(filepath=gltf_file)

# Register the panel and operator
def register():
    bpy.utils.register_class(MultipleGLTFImporterPanel)
    bpy.utils.register_class(ImportButton)

def unregister():
    bpy.utils.unregister_class(MultipleGLTFImporterPanel)
    bpy.utils.unregister_class(ImportButton)

if __name__ == "__main__":
    register()
