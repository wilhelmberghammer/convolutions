import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

from src.convolution import convolution


image = misc.ascent()

kernal = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]

processed_img = convolution(image, kernal)


plt.gray()
plt.axis('off')
plt.imshow(processed_img)
plt.show()