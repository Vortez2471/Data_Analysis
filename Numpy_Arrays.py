import numpy as np

my_list=[1,2,3]

print(np.array(my_list))    #converts list into array

my_matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(np.array(my_matrix))   #converts list into 2-D array

# BUILT-IN METHODS

# arange method
print(np.arange(0,10))
print(np.arange(0,11,2))

# zeros and ones
print(np.zeros(3))
print(np.ones((3,3)))

# linspace
print(np.linspace(0,10,3))
print(np.linspace(0,10,50))

# eye
print(np.eye(4))

# Random

# rand
print(np.random.rand(2))    #gives values between 0 and 1
print(np.random.rand(5,5))

# randn
print(np.random.randn(2))
print(np.random.randn(5,5))

# randint
print(np.random.randint(1,100))
print(np.random.randint(1,100,10))


# ARRAY ATTRIBUTES AND METHODS

arr=np.arange(25)
print(arr)
ranarr=np.random.randint(0,50,10)
print(ranarr)

# RESHAPE
arr.reshape(5,5)
print(arr)

# MAX,MIN,ARGMAX,ARGMIN

print(ranarr)
print(ranarr.max())
print(ranarr.argmax())
print(ranarr.min())
print(ranarr.argmin())

# SHAPE
print(arr.reshape(1,25).shape)
print(arr.reshape(1,25))
print(arr.reshape(25,1))
print(arr.reshape(25,1).shape)

print(arr.dtype)


