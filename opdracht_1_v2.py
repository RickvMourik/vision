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

def main():
    # Get the image and make a hsv copy of it
    imagefile = io.imread("colors.jpg")
    imagefileHSV = color.rgb2hsv(imagefile)
    
    # Make a copy of the image so there's an array which can be altered 
    recolored_image = copy.deepcopy(imagefile)

    # The matrix with which the rgb values have to be multiplied to make grey
    grayscale_matrix = np.array([0.2125, 0.7154, 0.0721])

    # loop through every pixel
    for pixel_row_index in range(len(imagefile)):
        for pixel_index in range(len(imagefile[pixel_row_index])):
            # if the pixel is not in this color spectrum "red", make it grey
            if not (imagefileHSV[pixel_row_index][pixel_index][0] > 0.08 and imagefileHSV[pixel_row_index][pixel_index][0] < 0.12):
                recolored_image[pixel_row_index][pixel_index] = recolored_image[pixel_row_index][pixel_index].dot(grayscale_matrix)
    
    # get a list with the hue values
    hue_original = get_hues(imagefile)
    color.rgb2hsv(recolored_image)
    hue_recolored = get_hues(recolored_image)

    hue_recolored = recolored_image[:,:,0]
    print(hue_recolored)
    hue_recolored = hue_recolored.flatten()
    print(hue_recolored)

    #create plots
    fig, axs = plt.subplots(2)
    num_bins = 36
    n, bins, patches = axs[0].hist(hue_original, num_bins, facecolor='blue', alpha=0.5)
    n, bins, patches = axs[1].hist(hue_recolored, num_bins, facecolor='red', alpha=0.5)
    axs[0].title.set_text('orginal')
    axs[1].title.set_text('recolored')
    plt.show()

    #grayscale = color.rgb2gray(imagefile)
    viewer = ImageViewer(recolored_image)
    viewer.show()

main()

# imagefileHSV[pixel_row_index][pixel_index][0] < 0.015 or imagefileHSV[pixel_row_index][pixel_index][0] > 0.95