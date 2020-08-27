import os
root_dir = os.getcwd()
#file_set = set()

for dir_, _, files in os.walk(root_dir):
    for file_name in files:
        rel_dir = os.path.relpath(dir_, root_dir)
        rel_file = os.path.join(rel_dir, file_name)
        print(rel_file)


#linux - 108
#mac - 170
#windows - 118
