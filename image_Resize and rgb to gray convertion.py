import glob
from PIL import Image
import cv2
from os import listdir, makedirs
import os

# for RGb to gray scale convertion


path = r'C:\Users\HP\Desktop\a'  # Source Folder
dstpath = r'C:\Users\HP\Desktop\c'  # Destination Folder

try:
    makedirs(dstpath)
except:
    print("Directory already exist, images will be written in asme folder")

# Folder won't used
files = os.listdir(path)

for image in files:
    img = cv2.imread(os.path.join(path, image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(dstpath, image), gray)


# for image resize

# Retrieving all image names and it's path with .jpg extension from given directory path in imageNames list
imageNames = glob.glob(r"C:\Users\HP\Desktop\c\*.jpg")

# Defining width and height of image
new_width = 500
new_height = 450

# Count variable to show the progress of image resized
count = 0

# Creating for loop to take one image from imageNames list and resize
for i in imageNames:
    # opening image for editing
    img = Image.open(i)
    # using resize() to resize image
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    # save() to save image at given path and count is the name of image eg. first image name will be 0.jpg
    img.save(r"C:\Users\HP\Desktop\b\\" + str(count) + ".jpg")
    # incrementing count value
    count += 1
    # showing image resize progress
    print("Images Resized" + str(count) + "/" + str(len(imageNames)), end='\r')

