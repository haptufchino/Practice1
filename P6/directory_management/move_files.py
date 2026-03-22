import shutil
import os

if os.path.exists("/storage/emulated/0/Download/pipis.txt"):
  shutil.move("/storage/emulated/0/Download/pipis.txt", "/storage/emulated/0/Download/deltrn")
  
f = "/storage/emulated/0/Download/The Second Sanctuary.mp3"
if not os.path.exists("/storage/emulated/0/Download/deltrn/The Second Sanctuary.mp3"):
  shutil.copy(f, "/storage/emulated/0/Download/deltrn")