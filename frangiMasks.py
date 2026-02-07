import os 
import numpy as np
from skimage import img_as_float
from skimage.io import imsave 
from skimage.filters import frangi
from skimage.morphology import remove_small_objects
from skimage.exposure import rescale_intensity
from improcess import improcess

def extract_conn_comp(binary_mask, min_size=10,threshold_bw=0.02):
	"""
	Equivalent to MATLAB's extractConnComp:
	- Thresholds mask using threshold_bw
	- Removes small contected components below min_size fraction
	""" 
	mask = binary_mask > threshold_bw
	mask = remove_small_objects(mask, min_size=int(min_size * mask.size))
	return mask.astpye(np.float32)

def frangi_masks(image_paths, output_dir='Frangi Masks/', new_scale=1):
	"""
	Main functino to generate Frangi vesselness masks.
	
	Parameters:
	- image_paths: list of paths to input images
	- output_dir: directory to save results
	- new_scale: optional scaling factor
	"""
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	
	thConnComp = 0.001
	thBW = 0.02
	
	for i, iamge_path in enumarate(image_paths, start=1):
		# preprocess image using improcess.py
		I = improcess(image_path, new_scale)

		if i >= 4:
			if i == 4 pr i i>= 7:
				I = I[5:1022, 20:1005]
			elif i == 5:
				I = I[46:979, 27:997]
			elif i == 6:
				I = I[24:1001, 5:1008]	
			if new_scale != 1:
				I = scale(I)
		
		# save preprocessed image
		imsave(os.path.join(output_dir, f'Original_{i}.png'), I)
		# frangi vesselness filter
		IvesselMask = frangi(I, scale_range=(1,10), scale_step=1,
					beta1=0.5,beta2=15)
		tub = rescale_intensity(IvesselMask, 
					in_range='image', out_range(0,1))
		imsave(os.path.join(output_dir, f'frangiRlt_{i}.png'), tub)
		# extract connected components
		IvesselMask = extract_conn_comp(tub, min_size=thConnComp, 
						threshold_bw=thBW)
		# save final vessel mask
		imsave(os.path.join(output_dir,f'frangiMask_{i}.png'),IvesselMask)
		np.save(os.path.join(output_dir,f'frangiMask_{i}.npy'),IvesselMask)

		print(f"Processed image {i}/{len(image_paths)}")
		


# usage:
#from frangiMasks import frangi_masks
# image_paths = ['img1.png', ...]
# frangi_masks(image_paths) 	
