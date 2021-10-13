import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)

    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while (result):
        ret,frame = videoCaptureObject.read()

        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
        return img_name
        print("snapshot taken")
        videoCaptureObject.release()
        cv2.destroyAllWindows()

take_snapshot()

def upload_files(img_name):
    access_token = "02LxqdKJrJwAAAAAAAAAAQegETfSYhEDeIXh8qfSKFT-FQrsdDOlgLx-LkDOn6yj"
    file = img_name
    file_from = file
    file_to = "/newFolder1/" + img_name
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("files are uploaded")

def main():

    while (True):
        if ((time.time() - start_time) >= 30):
            name = take_snapshot()
            upload_files(name)


main()