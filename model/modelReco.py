#from tensorflow.keras.models import load_model
#import cv2
#import numpy as np

def state(name):
    if name[0].isupper():
        if name[1].isupper():
            rep = 'Satisfaisant'
        else:
            rep = 'Good State'
    else:
        rep = 'New'
    return rep
