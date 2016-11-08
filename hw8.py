''' Homework 8
-- Due Monday, October 31th at 11:59pm
-- Before starting, read
https://www.cis.upenn.edu/~cis192/homework/
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
'''

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn import datasets
from sklearn import decomposition


def reduce_palette(img, n_colors):
    '''
    Use the sklearn k-means function to reduce the number of colors needed to
    represent an image.
    INPUTS: img, a string denoting the filepath of the image to be reduced.
            n_colors, the number of colors that your new image should
            represent
    OUTPUTS: A list of length w * h that features each pixel as a length 3
    numpy array. This list can be drawn to an image with the show_images()
    function we provide you so you can compare your output to the original
    picture. Neat! WARNING: k-means is very slow at large n_colors.
    Run this function at values above ~100 at your own risk.

    NOTES: For a larger image, run your kmeans on 1000 randomly selected
    pixels.
    If working on your own machine, you'll want to install the python
    image library  "pillow" for this problem. "pip3 install pillow" should do
    the trick.
    '''
    pass


def show_images(img, n_colors):
    '''
    This function is provided to you so that you may visually compare your color
    compressed output with the original image.
    INPUTS: img, the string containing the filepath of the original image to be
    compressed.

    WARNING: k-means is very, very slow at large n_colors. Run this function at
    n_colors above ~100 at your own risk.
    '''
    plt.figure(1)
    plt.clf()
    plt.axes([0, 0, 1, 1])
    plt.axis('off')
    plt.title('Original image (many colors)')
    shape = np.array(Image.open(img)).shape
    plt.imshow(np.array(Image.open(img)))

    pixel_list = np.array(reduce_palette(img, n_colors)).reshape(shape)

    plt.figure(2)
    plt.clf()
    plt.axes([0, 0, 1, 1])
    plt.axis('off')
    plt.title('Color-reduced image (K-Means)')
    plt.imshow(np.array(pixel_list, dtype=np.uint8))
    plt.show()


''' The following functions will walk you through the steps necessary to
perform PCA analysis on human faces and display the results. The faces come in
the form of 4096-length vectors containing brightness values for corresponding
pixels in images of the faces. '''


def preprocess():
    ''' Download the full dataset of faces in random order (completed for you).
    From this resulting matrix, complete the following adjustments:
    1. Compute the mean of each pixel across all such pixels. Calculate the mean
        of all 0th pixels, 1th pixels, ... 4095th pixels.
    2. Subtract from each pixel it  s corresponding mean.
    3. Compute the mean of each face vector.
    4. Subtract the mean of each face from each pixel in that face.
    OUTPUTS: An n_sample X 4096 numpy array of the preprocessed faces. '''
    dataset = datasets.fetch_olivetti_faces()

    # TODO: complete the rest of the function body


def get_decomposer():
    ''' Create a PCA decomposer. get_decomposer should take in keyword arguments
    that specify the number of components per sample (6 by default),
    the svd_solver method ('randomized' by default), and whether or not to
    whiten the sample to improve predictive accuracy (True by default).

    NOTE: The function header is incomplete as-is! '''
    pass


def gen_PCs(data, decomposer):
    ''' Taking in some n_sample X n_features matrix and some PCA decomposition
    model, decompose the matrix and return the collection of decomposed
    components. '''
    pass


def decompose():
    ''' If the above is done correctly, decompose() should run without error and
    display the preprocessed faces as well as the principal components of these
    faces. '''
    data = preprocess()
    decomposer = get_decomposer()
    decomposed_data = gen_PCs(data, decomposer)
    plot_gallery('Preprocessed Original Images', data[:6])
    plot_gallery('Principal Faces (The Eigenfaces!)', decomposed_data[:6])
    plt.show()


def plot_gallery(title, images, n_col=3, n_row=2):
    ''' This function is provided to you to visualize the data. You can change
    it if you need. '''
    plt.figure(figsize=(2. * n_col, 2.26 * n_row))
    plt.suptitle(title, size=16)
    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())
        plt.imshow(comp.reshape((64, 64)), cmap=plt.cm.gray,
                   interpolation='nearest',
                   vmin=-vmax, vmax=vmax)
        plt.xticks(())
        plt.yticks(())
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.93, 0.04, 0.)


def main():
    # test reduce_palette
    show_images("landscape.jpg", 25)

    # test preprocess, get_decomposer, gen_PCs
    decompose()

if __name__ == "__main__":
    main()
