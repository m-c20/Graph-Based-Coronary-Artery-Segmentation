import cv2
import numpy as np
from skimage import img_as_float
from skimage.color import rbg2gray
from skimage.transform import resize
from skimage.exposure import rescale_intensity#, adjust_sigmoid


def improcess(image_path, new_scale=1):
	# read image
	I = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
	
	# handle CMYK (4 channels)
	if I is none:
		raise ValueError("Image not found",image_path(

	if I.shape[-1] == 4:
		I = I[:,:,0] #take first channel

	# convert to grayscale if image is RGB

	if len(I.shape) == 3:
		I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

	#convert to [0,1]
	I = img_as_float(I)

"""
	# resize 
	if new_scale != 1:
		I = resize(I, (int(I.shape[0] * new_scale),
				int(I.shape[1]* new_scale)),
			perserve_range=True) 
		# matvlan mat2gray equivalent

		I = rescale_intensity(I, in_range='image',out_range=(0,1))
		#I = adjust_sigmoid(I)
		# imadhust equivalent to contrast stretching
		p2, p98 = np.precentile(I,(2,98))
		I = rescale_intensity(I, in_range(p2,98), out_range(0,1)) 
"""
	return I


	
