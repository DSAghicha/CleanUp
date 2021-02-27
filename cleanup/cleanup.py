""""This is the main script"""
import os
import shutil


def cleanup(file_path):
    os.chdir(file_path)
    print("Extracting files from " + file_path)
    files = [file for file in os.listdir(file_path) if os.path.isfile(file)]
    if not files:
        print("\nCould not find any files in the given directory!")
        exit(0)
    else:
        print("\nFound following files:")
        print("\n".join(files))
    ext = [val.split('.')[1] for val in files]
    print()
    for extension in set(ext):
        if os.path.exists(file_path + '\\' + extension):
            print("Directory Exists!")
        else:
            os.makedirs(extension)
            print("Created Directory: " + extension)

    print()

    for file, extension in zip(files, ext):
        if extension in file:
            if os.path.exists(file_path + '\\' + extension + '\\' + file):
                print("{} exist in the {}!".format(file, extension))
            else:
                shutil.move(file_path + '\\' + file, file_path + '\\' + extension)
                print("{} moved into the {}!".format(file, extension))
        else:
            print("Ran into some problem! Contact owner.")

    print("\nJob Successfully done!\n\nThank you for using CleanUp v1.0")
