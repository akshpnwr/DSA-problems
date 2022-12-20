import numpy as np
# from numpy import *

# arr = np.array([1,2,3])

# print(arr)

# print(np.zeros(3))
# print(np.ones(3))
# print(np.empty(5))

# print(np.arange(10))
# 
# print(np.arange(0,10))

# print(np.linspace(0,10,num=3))

# print(np.ones(3,dtype=np.int64))

# print(np.ones())
# print(zeros(4,dtype=int64))


# arr = np.array([2,1,4,5,7,9,6,8,3])

# print(np.sort(arr)) -> returns copy, arr is not mutated

# print(arr)

# a = np.array([[[1,2]],[[3,4]]])
# b = np.array([[[5,6]]])

# newArr = np.concatenate((a,b),axis=0)

# print(newArr)
# print(newArr.ndim)
# print(newArr.size)
# print(newArr.shape)


# a = np.arange(8)
# b = np.array([[[0,1]],[[2,3]],[[4,5]],[[6,7]]])
# b = np.array([[1,2],[3,4]])


# print(b.shape)
# print(a.reshape(4,2).shape)

# l1 = [1,2,3]

# arr= np.array(l1)

# print(type(l1))
# print(type(arr))


# i = (x*x for x in range(8))

# arr = np.fromiter(i,dtype=int)

# print(arr)
# print(next(i))
# print(next(i))
# print(next(i))


# print(np.empty([4,3],dtype=np.int32,order='C'))
# print(np.empty(5, dtype=np.int64))

# a = np.array([0,1,2,3,4,5,6])
# print(a[-5:])
# print(a[2:2:])

# a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# seven_up = (a>=7)

# print(a[seven_up])

# a = np.arange(5,dtype=float)
# b= np.arange(5,10)


# c = np.array([a,b])

# print(c)
# print(np.transpose(c))
# print(a)
# print(np.sum(a))
# print(np.sqrt(a))

# print(np.add(a,b))
# print(np.sum(a+b))

# a = np.arange(0,120,30)

# # print(a)

# b = np.sin(a*(np.pi/180))

# print(b)

# print(np.round(b,2))
# print(np.around(b,2))

# a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])

# print(np.floor(a))
# print(np.ceil(a))

# a = np.array([[1,2],[3,4],[5,6]])

# print(a)
# # print(np.shape(a))
# # print(a.itemsize)

# (3,2)
# # [[1,2,3], [4,5,6]]
# a.shape = (2,3)
# print(a)

# print(a.shape)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# print(a.reshape(3,2,2))
# print(a[1][1])
# print(a[::2])
# print(a[::2][1:])
# print(a.reshape((1,12)))
# print(a[...,1:])


# print(np.random.rand())

# print(np.random.rand(5,3))

arr = np.arange(1,11).reshape(2,5)

np.savetxt('array.txt',arr)

r = np.loadtxt('array.txt')
print(r)