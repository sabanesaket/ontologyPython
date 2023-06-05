import os
currentDir = os.getcwd()
print(currentDir)
parent_dir = os.path.dirname(currentDir)
file_name = 'Final.owl'
file_path = os.path.join(parent_dir, file_name)
print(file_path)