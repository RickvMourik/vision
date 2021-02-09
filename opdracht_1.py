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
import copy

def get_hues(image_data):
    hue= []
    for row in image_data:
        for pixel in row:
            hue.append(pixel[0])
    return hue

def main():
    imagefile = io.imread("colors.jpg")
    recolored_image = copy.deepcopy(imagefile)
    grayscale_matrix = np.array([0.2125, 0.7154, 0.0721])

    # loop through every pixel
    for pixel_row_index in range(len(imagefile)):
        for pixel_index in range(len(imagefile[pixel_row_index])):
            if (imagefile[pixel_row_index][pixel_index][0] > 165 and  imagefile[pixel_row_index][pixel_index][1] < 150 and imagefile[pixel_row_index][pixel_index][2] < 150) and (imagefile[pixel_row_index][pixel_index][1] < imagefile[pixel_row_index][pixel_index][2] + 15) :
                recolored_image[pixel_row_index][pixel_index] = imagefile[pixel_row_index][pixel_index]  
            else:
                recolored_image[pixel_row_index][pixel_index] = imagefile[pixel_row_index][pixel_index].dot(grayscale_matrix)
    
    # transform rgb to hsv for hue
    color.rgb2hsv(imagefile)
    hue_original = get_hues(imagefile)
    color.rgb2hsv(recolored_image)
    hue_recolored = get_hues(recolored_image)

    #create plots
    fig, axs = plt.subplots(2)
    num_bins = 36
    n, bins, patches = axs[0].hist(hue_original, num_bins, facecolor='blue', alpha=0.5)
    n, bins, patches = axs[1].hist(hue_recolored, num_bins, facecolor='red', alpha=0.5)
    plt.show()

    #grayscale = color.rgb2gray(imagefile)
    viewer = ImageViewer(recolored_image)
    viewer.show()

main()