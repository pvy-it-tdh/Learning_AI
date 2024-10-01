import numpy as np

# Create array
a = np.array([1, 2, 3, 4])

# Create array with all values being 0
zeros_array = np.zeros((2, 3))
# Output: [[0. 0. 0.]
#          [0. 0. 0.]]
print(zeros_array)

# Create array with all values being 1
ones_array = np.ones((2, 3))
# Output: [[1. 1. 1.]
#          [1. 1. 1.]]
print(ones_array)

# Create array with all values being a specified value
full_array = np.full((2, 3), 7)
# Output: [[7 7 7]
#          [7 7 7]]
print(full_array)
