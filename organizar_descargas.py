import os
import shutil


ext_video = [".mp4", ".srt", ".mkv"]
ext_app = [".apk"]
ext_foto = [".jpg", ".png"]
ext_music = [".mp3"]
ext_compressed = [".zip", ".rar"]
ext_docs = [".pdf", ".doc", ".txt"]
ext_torrent = [".torrent"]


os.chdir("C:/Users/satou/Downloads")
downloads_path = "C:/Users/satou/Downloads/"

def moveFile(extentionList, destFolder):
    for i in extentionList:
        if file_ext == i:
            shutil.move(downloads_path + f, downloads_path + destFolder)

def filesToRemove(extentionList):
    for i in extentionList:
        if file_ext == i:
            os.remove(downloads_path + f)

if __name__ == '__main__':
    
    for f in os.listdir():
        file_name, file_ext = os.path.splitext(f)
        #print(file_name, file_ext)
        moveFile(ext_video, "Video")
        moveFile(ext_foto, "Fotos")
        moveFile(ext_app, "apk")
        moveFile(ext_music, "Music")
        moveFile(ext_compressed, "Compressed")
        moveFile(ext_docs, "Documents")
        filesToRemove(ext_torrent)


