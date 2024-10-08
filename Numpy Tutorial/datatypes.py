import numpy as np


a = np.array([[1,2,3],
             [3,"Hello",5],
             [4,5,6]])
print(a)
print(a.dtype)  
#we can see that the datatpye is no longer int32 but <U11 which means there is less than 11 characters
#the dtype is string.

print(type(a[1][1]))