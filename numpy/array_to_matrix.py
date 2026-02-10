import numpy as np

#Reshaping
arr = np.arange(1, 13)
reshaped = arr.reshape((3, 4))
print(reshaped)

# Adding Arrays
arr1 = np.arange(1, 6)
arr2 = np.arange(6, 11)

# horizontal
hstack = np.hstack((arr1, arr2))
print(hstack)

# vertical
vstack = np.vstack((arr1, arr2))
print(vstack)