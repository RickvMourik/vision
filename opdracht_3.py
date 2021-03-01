import skimage
from skimage import data
from skimage.viewer import ImageViewer
from skimage import io
from skimage import color
from skimage import util
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import numpy as np
import math as math

def show_before_after(image, matrix):
    viewer = ImageViewer(image)
    viewer.show()

    transform_matrix = skimage.transform.AffineTransform(matrix = matrix)
    transformed = skimage.transform.warp(image, transform_matrix)

    viewer = ImageViewer(transformed)
    viewer.show()


def main():
    # Get the image and make a hsv copy of it
    imagefile = io.imread("crabdog.jpg")
    
    # translate the image
    translate_matrix = np.array([[1,0,140],[0,1,-125],[0,0,1]])
    show_before_after(imagefile, translate_matrix)

    # stretch the image
    stretch_matrix = np.array([[0.6,0,0],[0,2,0],[0,0,1]])
    show_before_after(imagefile, stretch_matrix)

    # rotate the image
    rotate_matrix = np.array([[math.cos(45), -math.sin(45), 0], [math.sin(45), math.cos(45), 0],[0,0,1]])
    show_before_after(imagefile, rotate_matrix)
    
    # rotate image 45 degrees, make it 2x as big, make it centred on the x-axis
    combo_matrix = np.matmul(np.matmul(np.array([[1,0,len(imagefile[0])/2],[0,1,0],[0,0,1]]), np.array([[0.5,0,0],[0,0.5,0],[0,0,1]])), rotate_matrix)
    show_before_after(imagefile, combo_matrix)



main()