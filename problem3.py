import os

# select the directory you want to list 
directory_path = '/'
# List all  file and directory in the specified path 
contents = os.listdir(directory_path)

# print each  file and directory name 
for  item in contents:
    print(item)
    