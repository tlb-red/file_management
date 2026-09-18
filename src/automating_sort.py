import shutil
import os
import config
import pathlib as Path
 
def main():
    source_folder = input("Enter source folder: ")
    move_files(source_folder)
    
def move_files(src): 
    all_files = os.listdir(src)
    files = [f for f in all_files if os.path.isfile(src + '/' + f)]
    home_directory = os.environ.get("HOME")
 
    for file in files:
        root, extension = os.path.splitext(file)
        formatted_extension = extension.split(".")[-1]
        
        if formatted_extension in config.DOCUMENT_FILE_TYPES:
            try:
                os.mkdir(f"{home_directory}/Documents/{formatted_extension.upper()}")
            except FileExistsError:
                print(f"Directory 'f{home_directory}/Documents/{formatted_extension.upper()}' already exists")
            except PermissionError:
                print(f"Permission denied: Unable to create 'f{home_directory}/Documents/{formatted_extension.upper()}'")

            source_folder = f"{src}/{file}"
            destination_folder = f"{home_directory}/Documents/{formatted_extension.upper()}/{file}"
            shutil.move(source_folder, destination_folder)

        elif formatted_extension in config.IMAGE_FILE_TYPES:
            try:
                os.mkdir(f"{home_directory}/Pictures/{formatted_extension.upper()}")
            except FileExistsError:
                print(f"Directory 'f{home_directory}/Pictures/{formatted_extension.upper()}' already exists")
            except PermissionError:
                print(f"Permission denied: Unable to create 'f{home_directory}/Pictures/{formatted_extension.upper()}'")

            source_folder = f"{src}/{file}"
            destination_folder = f"{home_directory}/Pictures/{formatted_extension.upper()}/{file}"    
            shutil.move(source_folder, destination_folder)

if __name__ == "__main__":
    main()