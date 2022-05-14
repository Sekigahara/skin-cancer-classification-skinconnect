import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im


class Helper:
    def __init__(self, array):
        self.array = array[:-1]
        self.label = label[-1]

    def reshape(self, new_shape):
        if type(new_shape) != tuple:
            raise TypeError("Tuple Only !")
        result = np.reshape(self.array, new_shape)
        return result

    def show_image(self):
        fig, ax = plt.show()
        ax.imshow(self.array)
        ax.set_label(self.label)
        plt.show()
