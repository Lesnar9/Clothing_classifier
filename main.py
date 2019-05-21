import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.preprocessing import image
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D,BatchNormalization,AveragePooling2D,Flatten,Softmax,Input,Dense,Dropout
from keras.models import Model
from keras.activations import relu,sigmoid,tanh