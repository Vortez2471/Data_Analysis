import numpy as np

arr=np.arange(0,11)
print(arr)

# BRACKET INDEXING AND SELECTION
print(arr[8])
print(arr[1:5])
print(arr[0:5])

# BROADCASTING        this makes numpy arrays different from list

arr[0:5]=100
print(arr)

arr=np.arange(0,11)
print(arr)

slice_of_arr=arr[0:6]    # it acts as reference
print(slice_of_arr)

slice_of_arr[:]=99
print(arr)

arr_copy=arr.copy()
print(arr_copy)

# INDEXING A 2-D ARRAY

arr_2d=np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

print(arr_2d[1])
print(arr_2d[1][0])
print(arr_2d[1,0])
print(arr_2d[:2,1:])

print(arr_2d[2])
print(arr_2d[2,:])

# FANCY INDEXING

arr2d=np.zeros((10,10))
arr_length=arr2d.shape[1]

for i in range(arr_length):
    arr2d[i]=i
print(arr2d)

print(arr2d[[2,4,6,8]])
print(arr[[6,4,2,7]])

# SELECTION

arr=np.arange(1,11)
print(arr)
print(arr>4)

bool_arr=arr>4
print(arr[bool_arr])

print(arr[arr>2])
x=2
print(arr[arr>x])