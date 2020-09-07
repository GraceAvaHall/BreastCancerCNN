

import sys
from glob import glob
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.image import imread
from shutil import copyfile
import os



def main(argv):
    magnification = argv[0]
    images, types = get_image_paths(magnification) # here
    move_images(images, magnification)
    sample_images = get_sample_images(images)
    #show_sample_images(sample_images)
    #print_labels(types)
    

def get_sample_images(images):
    sample_images = defaultdict(list)

    for label in images:
        for image_path in images[label][:5]:
            img = imread(image_path)
            sample_images[label].append(img)

    return sample_images


def show_sample_images(sample_images):
    xdim = 3
    ydim = len(sample_images)

    fig, axes = plt.subplots(ydim, xdim, figsize=(9, 16))
    for j, subtype in enumerate(sample_images):
        subtype_images = sample_images[subtype]
        for i in range(xdim):
            axes[j, i].imshow(subtype_images[i])
            axes[j, i].axes.xaxis.set_visible(False)
            axes[j, i].axes.yaxis.set_visible(False)
        axes[j, 0].set_ylabel(subtype)
        axes[j, 0].axes.yaxis.set_visible(True)

    plt.show()


def print_labels(types):
    for key, val in types.items():
        print('{:30}{:30}'.format(key, val))



if __name__ == '__main__':
    main(sys.argv[1:])




'''
def get_magnification_filenames(magnification):
    magnification_image_paths = glob(f'*/*/*/*/{magnification}/*.png') 
    
    images = defaultdict(list)

    for path in magnification_image_paths:
        path = path.split('\\')
        label = path[2]
        path = '/'.join(path)
        images[label].append(path)
        
    types = {}
    for label in images:
        suptype = images[label][0].split('/', 1)[0]
        types[label] = suptype

    return images, types


def move_images(images, magnification):
    os.mkdir(magnification)
    for label, pathlist in images.items():
        label_directory = magnification + '/' + label
        os.mkdir(label_directory)
        for img_path in pathlist:
            new_path = label_directory + '/' + img_path.rsplit('/', 1)[1]
            copyfile(img_path, new_path)
            
'''