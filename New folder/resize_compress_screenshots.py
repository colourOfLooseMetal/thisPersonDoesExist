import cv2
import os

path = os.getcwd()
qual = 72

def load_files_from_folder(folder):
    e = 0
    for filename in os.listdir(folder):
        # For every video file that is a mp4 in the folder
        if filename.endswith(".png"):
            e += 1
            newFname = str(e) + ".jpg"
            #print(filename)
            img = cv2.imread(folder + filename)
            height,width = img.shape[0:2]
            #print(height)
            #print(width)
            newWidth = int(width * 5)
            margin = int((width - newWidth)/2)
            crop_img = img[0:height, margin:margin+newWidth]
            resize = cv2.resize(img, (int(width*3.75), int(height*3.75)))
            cv2.imwrite("./rs/" + newFname, resize,
                        [int(cv2.IMWRITE_JPEG_QUALITY), qual])


load_files_from_folder(path + "./")
