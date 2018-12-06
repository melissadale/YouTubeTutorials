from PIL import Image
import glob
import random
import os
from collections import defaultdict

#################################
test_percentage = 0.20


def partitionRankings(rawRatings, testPercent):
    # https://stackoverflow.com/questions/23299099/trying-to-split-list-by-percentage
    howManyNumbers = int(round(testPercent*len(rawRatings)))
    shuffled = rawRatings[:]
    random.shuffle(shuffled)
    return shuffled[howManyNumbers:], shuffled[:howManyNumbers]


#################################################################
####    Make Directories (if needed)
#################################################################
caboodle = defaultdict(list)
categories = [x[1] for x in os.walk('./DATA')][0]

if 'train' in categories:
    categories.remove('train')
    categories.remove('validate')

for category in categories:
    val_dir = 'DATA/validate/'+str(category)
    train_dir = 'DATA/train/'+str(category)
    subdata = []

    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    if not os.path.exists(train_dir):
        os.makedirs(train_dir)


    #  Read images (currently either png or jpg format)
    for filename in glob.glob('DATA/'+str(category)+'/*.jpg'):
        im = Image.open(filename)
        keep = im.copy()
        subdata.append(keep)
        im.close()

    for filename in glob.glob('DATA/'+str(category)+'/*.png'):
        im = Image.open(filename)
        keep = im.copy()
        subdata.append(keep)
        im.close()


    random.shuffle(subdata)
    train_sample, test_sample = partitionRankings(subdata, test_percentage)

    #  Read images (save shuffled images to new train/validate folders in a jpg format)
    for i in range(len(train_sample)):
        train_sample[i].save(train_dir+'/'+str(category) + str(i) + '.jpg')

    for i in range(len(test_sample)):
        test_sample[i].save(val_dir+'/'+str(category) + str(i) + '.jpg')

#################################################################
####    Make labels.txt
#################################################################
f = open('DATA/labels.txt', 'w')

for category in categories:
        f.write(category+'\n')
f.close()
