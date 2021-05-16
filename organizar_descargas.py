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

def move_files(extention_list, dest_folder):
    for i in extention_list:
        if file_ext == i:
            shutil.move(downloads_path + f, downloads_path + dest_folder)

def remove_files(extention_list):
    for i in extention_list:
        if file_ext == i:
            os.remove(downloads_path + f)


if __name__ == '__main__':
    
    for f in os.listdir():
        file_name, file_ext = os.path.splitext(f)
        #print(file_name, file_ext)
        move_files(ext_video, "Video")
        move_files(ext_foto, "Fotos")
        move_files(ext_app, "apk")
        move_files(ext_music, "Music")
        move_files(ext_compressed, "Compressed")
        move_files(ext_docs, "Documents")
        remove_files(ext_torrent)


