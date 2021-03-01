import skimage
from skimage import data, filters
from skimage.viewer import ImageViewer
import scipy
from scipy import ndimage
import numpy as np


def opdracht_2_1(image):
    print("edge detection masks")
    # blurring
    blur_mask =[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
    newimage = scipy.ndimage.convolve(image, blur_mask)
    newimage = scipy.ndimage.convolve(newimage, blur_mask)

    viewer = ImageViewer(newimage)
    viewer.show()

    #edging
    #horizontal edge
    edge_mask1 = [[-4,0,4], [-4,0,4], [-4,0,4]]
    #vertical edge
    edge_mask2 = [[-1,-2,-1], [0,0,0], [1,2,1]]
    # diagonal edge towards the north east
    edge_mask3 = [[-3,-3,-3], [-3,0,5], [-3,5,5]]

    edgeimage1 = scipy.ndimage.convolve(image, edge_mask1)
    edgeimage2 = scipy.ndimage.convolve(image, edge_mask2)
    edgeimage3 = scipy.ndimage.convolve(image, edge_mask3)

    #show the edge detection
    viewer = ImageViewer(edgeimage1)
    viewer.show()

    viewer = ImageViewer(edgeimage2)
    viewer.show()

    viewer = ImageViewer(edgeimage3)
    viewer.show()
    return

def opdracht_2_2(image):
    print("build in edge detection")
    # build-in edge detection
    prewittimage = skimage.filters.prewitt(image)
    viewer = ImageViewer(prewittimage)
    viewer.show()

    robertsimage = skimage.filters.roberts(image)
    viewer = ImageViewer(robertsimage)
    viewer.show()

    faridimage = skimage.filters.farid(image)
    viewer = ImageViewer(faridimage)
    viewer.show()

    return

def opdracht_2_3(image):
    print("trying out sobel")
    cannyimage = skimage.feature.canny(image, sigma= 1.7, low_threshold= 40, high_threshold= 55)
    viewer = ImageViewer(cannyimage)
    viewer.show()

    return

def main():
    image = data.camera()
    #viewer = ImageViewer(image)
    #viewer.show()
    print('Give the exercise or all:')
    excerise = input()
    if excerise == "1":
        opdracht_2_1(image)
    elif excerise == "2":
        opdracht_2_2(image)
    elif excerise == "3":
        opdracht_2_3(image)
    else:
        opdracht_2_1(image)
        opdracht_2_2(image)
        opdracht_2_3(image)

main()