from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import glob
from PIL import Image
import os



outpath = "flipped/good"
if not os.path.exists(outpath):
    os.makedirs("flipped/good")



# Generates an array with the images from the folder:

img_dir = "images" # the image directory
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path)
data = []
for f1 in files:
    data.append(f1)

count=0
for j in data:

    image_obj = Image.open(j)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)

    src_fname, ext = os.path.splitext(j) 
    
    save_fname = os.path.join(outpath, os.path.basename(src_fname)+str(count)+'.jpg')
    rotated_image.save(save_fname)
    count+=1