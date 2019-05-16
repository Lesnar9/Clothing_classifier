import numpy as np
# impoort pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import scipy
from keras.preprocessing.image import image
def Load_Dataset():
    images = []
    for i in range (1,15001):
        path = 'Data/train/'+ str(i)+ '.jpg'
        try:
            im = image.load_img(path, target_size=(600, 600))
            x = image.img_to_array(im)
            images.append(x)
        except:
            pass

    return images

# im = image.load_img('Data/train/23.jpg',target_size = (600,600))
# x = image.img_to_array(im)
