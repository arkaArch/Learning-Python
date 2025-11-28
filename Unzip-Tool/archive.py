import zipfile, pathlib

def make_archive(file_paths, destination_folder):
    destination_folder_path = pathlib.Path(destination_folder, "compressed.zip")
    #- We can hardcoded this as: destination_folder_path = (destination_folder + "/" + "compressed.zip") but, in
    #- different operating system we have different naming convention(like in windows - "\" instead of "/"), which is
    #- handled by pathlib smartly

    with zipfile.ZipFile(destination_folder_path, 'w') as archive:
        for filepath in file_paths:
            # archive.write(filepath)
            #- Now the problem with the upper code is that "make_archive" function derived the
            #- destination folder path from filepath, so when we unzip the zip file it makes
            #- absolute_path_of_file like directory structor inside the "compressed" folder.
            #- To get rid of this problem we can use "arcname" argument and give to it the
            #- value of filename without its path.
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

# Test without running in case of main:
if __name__ == "__main__":
    make_archive(file_paths=["files/a.txt", "files/b.txt"], destination_folder="files")