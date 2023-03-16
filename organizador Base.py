from PIL import Image
import os



rutaActual = os.path.dirname(os.path.abspath(__file__))

def formatRuta(ruta):
    clean = ''
    for caracter in ruta:
        if caracter == '\\':
            clean = clean + '/'
        else:
            clean = clean + caracter

    return clean



downloadsFolder = formatRuta(r"C:\Users\UzielM\Documents\pruebaFoto") + '/'


organized_files = downloadsFolder + '/ArchivosOrganizados'
organized_filesImages = downloadsFolder + '/ArchivosOrganizados/ImagenesDescargadas'
organized_filesAudios = downloadsFolder + '/ArchivosOrganizados/AudiosDescargados'
organized_filesVideos = downloadsFolder + '/ArchivosOrganizados/VideosDescargados'
organized_filesPoint = downloadsFolder + '/ArchivosOrganizados/PowerPointDescargados'
organized_filesExe = downloadsFolder + '/ArchivosOrganizados/ProgramasDescargados'
organized_filesRar = downloadsFolder + '/ArchivosOrganizados/RARdescargados'
organized_filesWord = downloadsFolder + '/ArchivosOrganizados/WordDescargados'
organized_filesTxt = downloadsFolder + '/ArchivosOrganizados/ArchivosTxt'
organized_filesPdf = downloadsFolder + '/ArchivosOrganizados/PDFDescargados'

os.mkdir(organized_files)
os.mkdir(organized_filesImages)
os.mkdir(organized_filesAudios)
os.mkdir(organized_filesVideos)
os.mkdir(organized_filesPoint)
os.mkdir(organized_filesExe)
os.mkdir(organized_filesRar)
os.mkdir(organized_filesWord)
os.mkdir(organized_filesTxt)
os.mkdir(organized_filesPdf)


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(organized_filesImages + '/' + "compressed_" + filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
#            print(name + ": " + extension)

        if extension in [".mp3", ".flac"]:
            os.rename(downloadsFolder + filename, organized_filesAudios + '/' + filename)

        if extension in [".mp4", ".mov"]:
            os.rename(downloadsFolder + filename, organized_filesVideos + '/' + filename)

        if extension in [".pptx"]:
            os.rename(downloadsFolder + filename, organized_filesPoint + '/' + filename)

        if extension in [".exe"]:
            os.rename(downloadsFolder + filename, organized_filesExe + '/' + filename)

        if extension in [".rar", ".zip"]:
            os.rename(downloadsFolder + filename, organized_filesRar + '/' + filename)

        if extension in [".docx"]:
            os.rename(downloadsFolder + filename, organized_filesWord + '/' + filename)

        if extension in [".txt"]:
            os.rename(downloadsFolder + filename, organized_filesTxt + '/' + filename)

        if extension in [".pdf"]:
            os.rename(downloadsFolder + filename, organized_filesPdf + '/' + filename)