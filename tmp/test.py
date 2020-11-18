import skimage
from skimage import filters
import matplotlib.pyplot as plt

img = skimage.data.hubble_deep_field()
img = skimage.color.rgb2gray(img)
flt = filters.prewitt(img)
plt.imshow(flt, cmap='gray')
plt.show()