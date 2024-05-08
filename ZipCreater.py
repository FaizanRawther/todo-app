import zipfile
import pathlib

def make_archive(file_paths,dest_dirctory):
    dest_path=pathlib.Path(dest_dirctory,"compressed.zip")
    with zipfile.ZipFile(dest_path,"w") as archive:
        for filepath in file_paths:
            filepath=pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)

if __name__=="__main__":
    make_archive(file_paths=["todos.txt","exercise1gui.py"],dest_dirctory="compressed files")
