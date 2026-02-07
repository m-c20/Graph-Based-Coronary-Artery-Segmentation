import os
import numpy as np
from skimage import img_as_float
from skimage.io import imsave
from skimage.filters import frangi
from skimage.morphology import remove_small_objects
from skimage.exposure import rescale_intensity
from skimage.transform import resize

def scale(image, new_scale=1):
	p2, p98 = np.percentile(image, (2,98))
	I = resize(image,(int(image.shape[0]*new_scale), 
			int(image.shape[1]*new_scale),
			preserve_range=True))
	I = rescale_intensity(I, in_range='image',out_range=(0,1))
	I = rescale_intensity(I, in_range=(p2,p98), out_range=(0,1))
	return I


