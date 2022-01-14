"""
Clasificación usando k-NN - Digits Dataset
-----------------------------------------------------------------------------------------


"""
import matplotlib.pyplot as plt
from sklearn import datasets


def pregunta_01():
    """
    Complete el código presentado a continuación.

    """

    # Load the digits dataset: digits
    digits = datasets.load_digits()

    # Print the keys of the dataset
    print(digits.target_names)

    # Print the shape of the images and data keys
    print(digits.data.shape)
    print(digits.target.shape)

    # Display digit 1010
    plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.show()


def pregunta_02():
    """
    Complete el código presentado a continuación.

    """


pregunta_01()
