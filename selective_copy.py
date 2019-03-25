#! python3

# selective_copy.py - Search files with certain files extensions and copy these files to another folder.

# Import essential modules.
import os
import shutil

# Create variables with directory to check and directory to copies folder.
path_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects'
copies_path = r'C:\Users\ogi-8\Desktop\PythonProjects\SelectiveCopy\TXT_files'

# Use for loop and os.listdir to find files with wanted extension.
for file in os.listdir(path_to_check):
    if file.endswith('.txt'):

# Get abs path to matched file.
        file_path = os.path.abspath('..\\' + file)

# Print result and what will be done.
        print('Copy {} to {}'.format(file, copies_path))

# Copy wanted files to other destination.
        shutil.copy(file_path, copies_path)

# Change project status on github.
print('Done.')
