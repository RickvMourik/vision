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

def main():
    # Get the image and make a hsv copy of it
    imagefile = io.imread("crabdog.jpg")
    viewer = ImageViewer(imagefile)
    viewer.show()

    # translate the image
    translate_matrix = np.array([[1,0,140],[0,1,-125],[0,0,1]])
    transform_translate = skimage.transform.AffineTransform(matrix = translate_matrix)
    translated = skimage.transform.warp(imagefile, transform_translate)
    
    viewer = ImageViewer(translated)
    viewer.show()

    # stretch the image

    stretch_matrix = np.array([[0.6,0,0],[0,2,0],[0,0,1]])
    transform_stretch = skimage.transform.AffineTransform(matrix = stretch_matrix)
    stretched = skimage.transform.warp(imagefile, transform_stretch)
    
    viewer = ImageViewer(stretched)
    viewer.show()

    # rotate the image

    rotate_matrix = np.array([[math.cos(45), -math.sin(45), 0], [math.sin(45), math.cos(45), 0],[0,0,1]])
    transform_rotate =  skimage.transform.AffineTransform(matrix= rotate_matrix)
    rotated = skimage.transform.warp(imagefile, transform_rotate)

    viewer =  ImageViewer(rotated)
    viewer.show()

    # rotate image 45 degrees, make it 2x as big, make it centred on the x-axis
    
    combo = np.matmul(np.matmul(np.array([[1,0,len(imagefile[0])/2],[0,1,0],[0,0,1]]), np.array([[0.5,0,0],[0,0.5,0],[0,0,1]])), rotate_matrix)
    print(combo)
    transform_combo = skimage.transform.AffineTransform(matrix = combo)
    stretched = skimage.transform.warp(imagefile, transform_combo)
    
    viewer = ImageViewer(stretched)
    viewer.show()



main()