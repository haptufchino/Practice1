import os

os.makedirs("/storage/emulated/0/Download/deltrn/kris_char/dialogs", exist_ok=True)
print("Folders are created\n")

path = "."
for item in os.listdir(path):
    print(item)
print()

path = "/storage/emulated/0/Download/"
for file in os.listdir(path):
    if file.endswith(".mp3"):
        print(file)