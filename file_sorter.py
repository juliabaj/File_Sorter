import os
import shutil

#directory = os.path.join(os.path.expanduser("~"), "OneDrive", "Dokumenty") #don't have to define the path thanks to expanduser
directory = os.path.join(os.path.expanduser("~"), "PycharmProjects", "pythonProject")

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".mp3": "Music",
    ".csv": "Documents",
    ".dot": "Documents",
    ".wav": "Music",
    ".py": "Scripts"
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()   #"splitext" splits a filename for root[0] and extension[1]

        if extension in extensions:
            folder_name = extensions[extension]


            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)


            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder")
        else:
            print(f"Unknown file extention for {filename}")
    else:
        print(f"{filename} is a directory, not a file")

print("File organization is completed.")



