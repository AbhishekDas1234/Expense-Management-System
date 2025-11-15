import os
import sys

current_file_directory=__file__
root_directory=os.path.dirname(current_file_directory)
parent_directory=os.path.join(root_directory,'..')
sys.path.insert(0,parent_directory)

print(current_file_directory)
print(root_directory)
print(parent_directory)
print(sys.path)