"""
Here are some notes and frequently used numpy functions.
"""

# creating arrays
np.zeros()
np.ones()
np.zeros_like()
np.ones_like()
np.array()

# these are useful when we need to adjust the dimensions.
np.expand_dims(x, axis=0)
np.squeeze()
np.reshape(x, (1,2,3))
np.transpose(x, (1,2,0)) # permute axis.
#np.swapaxes(x, 0, 1) # this could be done by np.transpose().

# join/split arrays TODO
np.stack()
np.split()

# tile arrays
np.tile()

# serialization/deserialization TODO


# broadcast rules. https://numpy.org/devdocs/user/theory.broadcasting.html

# a numpy arithmetic operation, doesn't require the arrays to have exact shapes. 
# smaller arrays could be broadcasted to fit the larger array. 
# A's shape: (a1,a2,a3,a4), B's shape: (b1,b2,b3)
# the trailing axes are determined by aligning shapes to the right.
#    a1 x a2 x a3 x a4
#         b1 X b2 X b3

# operation works if the trailing axes have identical shapes, or on these dimensions one of the two is 1.
# Example #1
# A: 256 x 256 x 3
# B:             3

# Example #2
# A: 8 x 1 x 6 x 1
# B:     7 x 1 x 5

# to fill up the missing dimensions, the smaller will just copy itself along those dimensions.
# this is quite useful for vectorization and sppedup the computation in C instead of in Python.
# it can also be used to perform outer operations.

# element-wise multiplication (when shapes are the same. when it's not there is broadcast.)
x * y

# multiplications
np.dot()
np.matmul()


