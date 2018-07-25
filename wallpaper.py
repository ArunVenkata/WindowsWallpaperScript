import os, sys, re, shutil
import time
from PIL import Image


#Set Environment Variables
username = os.environ['USERNAME']


#Path for folder containing windows 10 Lockscreen Wallpapers
dir_src = ("C:\\Users\\"+ username +"\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\")


#Add Path of destination folder
dir_dst = ("C:\\Users\\"+ username +"\\Desktop\\New folder\\")

print("Deleting Files",end='')
time.sleep(1)
print(".",end='')
time.sleep(1)
print(".")
#(Warning!)Deletes all Files In Current Folder
for the_file in os.listdir(dir_dst):
    file_path = os.path.join(dir_dst, the_file)
    base_file, ext = os.path.splitext(the_file)
    if ext==".jpg":
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

print("Copying Wallpapers",end='')
time.sleep(1)
print(".",end='')
time.sleep(1)
print(".")           
#Copy All Wallpapers From Src Folder To Dest Folder
for filename in os.listdir(dir_src):
    shutil.copy( dir_src + filename, dir_dst)
    #print(filename)

print("Changing Extensions",end='')
time.sleep(1)
print(".",end='')
time.sleep(1)
print(".")
#Look into all the files in the executing folder and change extension
for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
  base_file, ext = os.path.splitext(filename)
  if ext == "":
    os.rename(filename, base_file + ".jpg")

print("Extracting Wallpapers",end='')
time.sleep(1)
print(".",end='')
time.sleep(1)
print(".")
#Remove all files Not having Wallpaper Resolution
for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
  base_file, ext = os.path.splitext(filename)
  if ext == ".jpg":
    im=Image.open(os.path.dirname(os.path.realpath(__file__)) + '\\' +filename)
    #print(list(im.size))
    if list(im.size)[0] != 1920 and list(im.size)[0] != 1080 :
      im.close()
      os.remove(os.path.dirname(os.path.realpath(__file__)) + '\\' +filename)
    else:
      im.close()
msg ='''
    DDDDD      OOOOO    NN      N  EEEEEEE
    D    D    O     O   N N     N  E
    D     D   O     O   N  N    N  E
    D     D   O     O   N   N   N  EEEE
    D     D   O     O   N    N  N  E
    D    D    O     O   N     N N  E
    DDDDD      OOOOO    N      NN  EEEEEEE
'''
print(msg)
time.sleep(3)
