from PIL import Image
import os, sys

path = "dataset/ආ/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            if item.endswith('jpg'):
                im = Image.open(path + item)
                f, e = os.path.splitext(path + item)
                imResize = im.resize((450, 800), Image.ANTIALIAS)
                imResize.save(f + '.jpg', quality=80)
                print("[INFO] Resizing "+f+".Jpg")
            else:pass


resize()