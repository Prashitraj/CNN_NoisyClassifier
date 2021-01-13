import os 
from PIL import Image
from tqdm import tqdm 
dir = "../data/noisy1/simple"
list = os.listdir(dir) # dir is your directory path
number_files = len(list)
print(number_files)


rdir = "../data/noisy1/rsimple"

images = []
for file in tqdm(list):
    image = Image.open(dir+"/"+file)
    rimage = image.resize((224,224))
    print(image.size,rimage.size)
    rimage.save(rdir+"/"+file)
