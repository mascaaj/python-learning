import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_img(img):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')

def load_img(image_name):
    image_path = '../../data/' + image_name
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def load_img2(image_name):
    image_path = '../../data/' + image_name
    img = cv2.imread(image_path)
    view_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img,view_img
