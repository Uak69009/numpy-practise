import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([[1.1,2.2,3.3,4.4],[5.5,6.6,7.7,8.8]])
a.shape
b.shape 
a.ndim
b.ndim 
# print (a.shape) # (5,) number of elements in the array
# print (b.shape)
# print(a.ndim) # dimension of the array
# print(b.ndim)

b[1:5] # prints the elements from the second to the fifth row of the array b
print(b[1,3]) # prints the element at the second row and fourth column of the array b

