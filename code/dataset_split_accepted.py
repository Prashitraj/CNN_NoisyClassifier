import os 
from tqdm import tqdm
rdir = "../data/accepted/simple"

list = os.listdir(rdir) # dir is your directory path
number_files = len(list)
print(number_files)

train = list[:8000]
val = list[8000:9000]
test = list[9000:]

for file in tqdm(train):
    os.rename(rdir+"/"+file,"../data/simple/train/accepted"+"/accepted_"+file)

for file in tqdm(val):
    os.rename(rdir+"/"+file,"../data/simple/validation/accepted"+"/accepted_"+file)

for file in tqdm(test):
    os.rename(rdir+"/"+file,"../data/simple/test/accepted"+"/accepted_"+file)
