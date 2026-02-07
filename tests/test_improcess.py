import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt 
from improcess import improcess as imp

# the image after running improcess python 
I_py = imp("7.png",new_scale=1)

# matlab result of same image 
mat = sio.loadmat("I_matlab.mat")
I_mat = mat["I"]

print("Shape MATLAB:",I_mat.shape)
print("Shape python:",I_py.shape)

print("Max abs diff:", np.max(np.abs(I_mat - I_py)))
print("Mean abs diff:", np.mean(np.abs(I_mat -I_py)))

import json

results = {
    "shape_matlab": I_mat.shape,
    "shape_python": I_py.shape,
    "max_abs_diff": float(np.max(np.abs(I_mat - I_py))),
    "mean_abs_diff": float(np.mean(np.abs(I_mat - I_py)))
}

with open("comparison_results.json", "w") as f:
    json.dump(results, f, indent=4)

import cv2
cv2.imwrite("I_python.png", (I_py*255).astype(np.uint8))

plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.title("MATLAB")
plt.imshow(I_mat, cmap="gray")
plt.axis("off")


plt.subplot(1,3,2)
plt.title("Python")
plt.imshow(I_py, cmap="gray")
plt.axis("off")

plt.subplot(1,3,3)
plt.title("Difference")
plt.imshow(np.abs(I_mat - I_py), cmap="hot")
plt.colorbar()
plt.axis("off")

plt.show()









