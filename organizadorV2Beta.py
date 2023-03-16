import os
from PIL import Image

def path_format(path):
    return path.replace('\\', '/')

folder_test = path_format(r"D:\FMelox\Documents\archivos escuela y mas")
organized_files = os.path.join(folder_test, 'FilesOrganizados')

extensions = {
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".gif": "Imagenes",
    ".mp3": "Audios",
    ".flac": "Audios",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
    ".ppt": "PowerPoints",
    ".pptx": "PowerPoints",
    ".doc": "DocWords",
    ".docx": "DocWords",
    ".rar": "Rars",
    ".zip": "Rars",
    ".exe": "EjecutablesExe",
    ".pdf": "DocPdfs",
    ".txt": "ArchivosTxt",
}

if not os.path.exists(organized_files):
    os.mkdir(organized_files)

for directory in set(extensions.values()):
    dir_path = os.path.join(organized_files, directory)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

for filename in os.listdir(folder_test):
    name, extension = os.path.splitext(filename)
    if extension.lower() in extensions:
        directory = extensions[extension.lower()]
        file_path = os.path.join(folder_test, filename)
        dir_path = os.path.join(organized_files, directory)
        if extension.lower() in [".jpg", ".jpeg", ".png", ".gif"]:
            try:
                picture = Image.open(file_path)
                picture.save(os.path.join(dir_path, filename))
                os.remove(file_path)
            except Exception as e:
                print(f"Error: Could not open {file_path}: {e}")
        else:
            os.rename(file_path, os.path.join(dir_path, filename))