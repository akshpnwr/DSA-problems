###################
#FIBBONACCI SERIES#
###################
# a, b = 0, 1

# while (a < 10):
#     print(a)
#     temp = a
#     a = b
#     b = temp + b

# x = int(input('Please enter an integer: '))
# if (x < 0):
#     print('negative')
# elif (x == 0):
#     print('zero')
# else:
#     print('postive')

# users = {'hans': 'active', 'eleonore': 'inactive', 'VHCSA': 'active'}

# for user, status in users.copy().items():
#     if (status == 'inactive'):
#         del users[user]

# print(users)

# a = ['akash', 'mayank', 'sahil', 'gnja']

# for i in range(len(a)):
#     print(i, a[i])

#################
#PLINDROME CHECK#
#################

# num = int(input('Please enter a number: '))
# temp = num
# b = 0
# while (temp != 0):
#     a = temp % 10
#     b = b*10+a
#     temp = int(temp/10)

# if (num == b):
#     print('Palindrome')
# else:
#     print('Not palindrome')

####################
#ENUMERATE FUNCTION#
####################

# x = ('apple', 'namama', 'cherry')
# # y = enumerate(x)

# # print(x, list(y))

# for i, fruit in enumerate(x):
#     print(i, fruit)


# nums = 12
# rev = []
# while nums != 0:
#     dig = nums % 10
#     rev.append(dig)
#     nums = nums//10

# org = rev

# print(org == rev[::-1])

# print(nums[::-1])

# target = 13

# prevMap = {}

# for key, num in enumerate(nums):
#     val = target-num
#     if (val in prevMap):
#         print([prevMap[val], key])
#         break
#     else:
#         prevMap[num] = key

# a = 10
# b = 5
# print("Before: ", a, b)

# a = a+b
# b = a-b
# a = a-b

# print("After: ", a, b)

'''
Practicing for python mid exam
'''

# a = '''
# tnhoaivjn,
# ahgcjanc,a
# uasgdjsa
# ahjc
# '''
# print(a)

# name = 'akash'

# age = int(input('Enter age '))
# name = input('Enter your name ')

# print(type(age))

# print('My name is {} and my age is {}'.format(name, age))

# _akash = 'akash'

# print(_akash)




# string = 'This is a war cry \'We are viking\' '
# s = 'Valhalla'

# # print(string.upper())
# # print(string.lower())
# # print(string.strip())
# # print(string.replace('war','WAR'))
# print(string + ' ' + s)

# v = 10_00000
# # print(type(100000))
# print(int(5/2))
# print(5//2)

# print(int(4**(1/2)))

# l = list((1,2,3,4))
# print(len(l))

# t = (1,2,'apple')
# t[0] = 0
# print(type(t))
# print(t[0])

# s1 = {5,1,3,4,2,3}
# s2 = {True, False, False}
# print(s1)
# print(s2)


# obj = {
#     'name': 'ajsdh',
#     'age': 22
# }

# print(obj['name'])

# obj = {
#     2: 1,
#     3:0,
#     1: 5,
#     4: 2
# }

# for i in sorted(obj.keys()):
#     print(i, end=' ')

# print()
# for i in sorted(obj.items()):
#     print(i, end=' ')


# from copy import copy, deepcopy


# list = [1,2,3,4,5]

# l = deepcopy(list)
# print(l)

# x='aditya'
# def outer():
#     x='akash'
#     def inner():
#         nonlocal x
#         x=x+' panwar'
#         print('inside inner ',x)

#     inner()

# outer()
# print(x)


# add = lambda a,b: a+b

# print(add(1,2))

# import functools


# l = [1,2,8,3,4,5]

# sum = lambda a,b: a+b
# max = lambda a,b: a if a>b else b
# print(functools.reduce(sum,l))
# print(functools.reduce(max,l))

import datetime

n = datetime.datetime.now()

d= datetime.date.today()
