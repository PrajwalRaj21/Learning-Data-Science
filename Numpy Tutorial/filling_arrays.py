import numpy as np

a = np.full((2,3,4), 9)
print(a)

#prints out 2 matrix with 3 lists and 4 elements each

a = np.zeros((10,5,2))
print(a) #prints0

a = np.ones((3,4,5))
print(a)  #prints 1

a = np.empty((5,5,5))
print(a)


#generating a range

x_values = np.arange(0, 100,5)  #0 is the starting, 1000 is the end and 5 is the step size
print(x_values)

x_values = np.linspace(0, 100, 2)
print(x_values)


y = np.diag(np.arange(3))
print(y)