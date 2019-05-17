
import numpy as np
from keras.preprocessing.image import image
from utils_1 import *
path = 'Data/train/'
images =np.zeros((99,600,600,3))
for i in range(1, 100):
    try:

        im = image.load_img(path + str(i) +'.jpg',target_size = (600,600))

        x = image.img_to_array(im)



        images[i-1,:,:,:] = x
    except:
        pass
