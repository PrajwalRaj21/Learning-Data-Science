import numpy as np

a  = [1,2,3,5,]
print(a)   #this is how we print list in pytohn


b = np.array([1,2,4,5,6])
print(b)  #the output is [1 2 4 5 6]. It gets printed without the comma
print(b[0])
print(type(b))  #type numpy ndarray
print(type(a))   #type list
print(b[1:3])
b[4] = 10
print(b)

