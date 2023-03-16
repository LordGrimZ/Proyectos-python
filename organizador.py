import os
from PIL import Image
ActualPath = os.path.dirname(os.path.abspath(__file__))

def PathFormat(path):
    return path.replace('\\', '/')


#folderTest = PathFormat(r"D:\FMelox\Documents\test2")
folders = ["OrganizedFiles","Imagenes", "Audios", "Videos", "PowerPoints",
            "DocWords", "Rars", "EjecutablesExe", "DocPdfs", "ArchivosTxt"]
for folder in folders:
    path = os.path.join(folderTest, folder)
    os.makedirs(path)

"""organizedFiles = folderTest + '/FilesOrganizados'
organizedFilesImagenes = folderTest + '/FilesOrganizados/Imagenes'
organizedFilesAudios = folderTest + '/FilesOrganizados/Audios'
organizedFilesVideos = folderTest + '/FilesOrganizados/Videos'
organizedFilesPPoint = folderTest + '/FilesOrganizados/PowerPoints'
organizedFilesWord = folderTest + '/FilesOrganizados/DocWords'
organizedFilesRar = folderTest + '/FilesOrganizados/Rars'
organizedFilesExe = folderTest + '/FilesOrganizados/EjecutablesExe'
organizedFilesPdf = folderTest + '/FilesOrganizados/DocPdfs'
organizedFilesTxt = folderTest + '/FilesOrganizados/ArchivosTxt' """



"""os.mkdir(organizedFiles)
os.mkdir(organizedFilesImagenes)
os.mkdir(organizedFilesAudios)
os.mkdir(organizedFilesVideos)
os.mkdir(organizedFilesPPoint)
os.mkdir(organizedFilesWord)
os.mkdir(organizedFilesRar)
os.mkdir(organizedFilesExe)
os.mkdir(organizedFilesPdf)
os.mkdir(organizedFilesTxt)"""


if __name__ == "__main__":
    for filename in os.listdir(folderTest):
        name,extension = os.path.splitext(folderTest + filename)
        if extension in [".jpg", ".jpeg",".png", ".gif"]:
            picture = Image.open(folderTest + filename)
            picture.save(organizedFilesImagenes +' /' + filename)
            os.remove(folderTest + filename)

        if extension in [".mp3", ".flac"]:
            os.rename(folderTest + filename, organizedFilesAudios + "/" + filename)

        if extension in [".mp4", ".mov", ".mkv" ]:
            os.rename(folderTest + filename, organizedFilesVideos + "/" + filename)

        if extension in [".ppt", ".pptx"]:
            os.rename(folderTest + filename, organizedFilesPPoint + "/" + filename)

        if extension in [".doc", ".docx"]:
            os.rename(folderTest + filename, organizedFilesWord + "/" + filename)

        if extension in [".rar", ".zip"]:
            os.rename(folderTest + filename, organizedFilesRar + "/" + filename)

        if extension in [".exe"]:
            os.rename(folderTest + filename, organizedFilesExe + "/" + filename)

        if extension in [".pdf"]:
            os.rename(folderTest + filename, organizedFilesPdf + "/" + filename)

        if extension in [".txt"]:
            os.rename(folderTest + filename, organizedFilesTxt + "/" + filename)
        
