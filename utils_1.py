import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
def Load_Dataset():
    a = pd.read_csv('Input/train_labels.csv')
    Y_train = np.array(a)
    b= pd.read_csv('Input/validation_labels.csv')
    Y_dev = np.array(b)
    return Y_train,Y_dev
#     images = []
#     for i in range (1,15001):
#         path = 'Data/train/'+ str(i)+ '.jpg'
#         try:
#             im = image.load_img(path, target_size=(600, 600))
#             x = image.img_to_array(im)
#             images.append(x)
#         except:
#             pass

#     return images


# im = image.load_img('Data/train/23.jpg',target_size = (600,600))
# x = image.img_to_array(im)
