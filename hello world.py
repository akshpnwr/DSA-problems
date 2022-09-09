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

a = 10
b = 5
print("Before: ", a, b)

a = a+b
b = a-b
a = a-b

print("After: ", a, b)
