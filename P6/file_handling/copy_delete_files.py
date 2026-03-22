import shutil
import os

shutil.copy("/storage/emulated/0/Download/pipis.txt", "/storage/emulated/0/Download/pipis_copy.txt")
print("The file is copied")
f = "/storage/emulated/0/Download/pipis_copy.txt"
if os.path.exists(f):
    os.remove(f)
    print("File is deleted")
else:
    print("File is not deleted")