#credit: Juan Carlos Niebles and Ranjay Krishna

import numpy as np

def conv_naive(image, kernel):
    """A naive implementation of convolution filter.

    This is a naive implementation of convolution using 4 nested for-loops.
    This function computes convolution of an image with a kernel and outputs
    the result that has the same shape as the input image.

    Args:
        image: numpy array of shape (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk)

    Returns:
        out: numpy array of shape (Hi, Wi)
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    for i in range(Hi):
        for j in range(Wi):
            for k in range(Hk):
                for l in range(Wk):
                    if i+k-Hk//2 >= 0 and i+k-Hk//2 < Hi and j+l-Wk//2 >= 0 and j+l-Wk//2 < Wi:
                        out[i, j] += image[i+k-Hk//2, j+l-Wk//2] * kernel[k, l]
    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return out

def zero_pad(image, pad_height, pad_width):
    """ Zero-pad an image.

    Example: a 1x1 image [[1]] with pad_height = 1, pad_width = 2 becomes:

        [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]         of shape (3, 5)

    Args:
        image: numpy array of shape (H, W)
        pad_width: width of the zero padding (left and right padding)
        pad_height: height of the zero padding (bottom and top padding)

    Returns:
        out: numpy array of shape (H+2*pad_height, W+2*pad_width)
    """

    H, W = image.shape
    out = None

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    out = np.zeros((H+2*pad_height, W+2*pad_width))
    out[pad_height:H+pad_height, pad_width:W+pad_width] = image
    ######################################
    #        END OF YOUR CODE            #
    ######################################
    return out


def conv_fast(image, kernel):
    """ An efficient implementation of convolution filter.

    This function uses element-wise multiplication and np.sum()
    to efficiently compute weighted sum of neighborhood at each
    pixel.

    Hints:
        - Use the zero_pad function you implemented above
        - There should be two nested for-loops
        - You may find np.flip() and np.sum() useful

    Args:
        image: numpy array of shape (Hi, Wi)
        kernel: numpy array of shape (Hk, Wk)

    Returns:
        out: numpy array of shape (Hi, Wi)
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    #####################################
    #       START YOUR CODE HERE        #
    #####################################
    image = zero_pad(image, Hk//2, Wk//2)
    kernel = np.flip(np.flip(kernel, 0), 1)
    for i in range(Hi):
        for j in range(Wi):
            out[i, j] = np.sum(image[i:i+Hk, j:j+Wk] * kernel)
    ######################################
    #        END OF YOUR CODE            #
    ######################################

    return out

