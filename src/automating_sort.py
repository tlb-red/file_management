import shutil
import os
import io
import config 
from pathlib import Path

    
def main():  
    path_origin = input("Enter src: ")
    path_dest = input("Enter dest: ") 
    files = os.listdir(path_origin)
    files = [f for f in files if os.path.isfile(path_dest + '/' + f)]

    for file in files:
        file_name = file.split(".")
        file_ext = file_name[1]
        for i in range(0, len(config.FILE_TYPES)):
            if file_ext == config.FILE_TYPES[i]:
                for j in range(0, len(config.FOLDER_TYPES)):
                    if file_ext.upper() == config.FOLDER_TYPES[j]:
                        folder_src = path_origin + '/' + file
                        folder_dest = path_dest + '/' + config.FOLDER_TYPES[j] + '/' + file
                        shutil.move(folder_src, folder_dest)

if __name__ == "__main__":
    main()