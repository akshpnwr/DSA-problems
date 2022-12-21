from matplotlib import pyplot as plt
# from numpy import *
from pandas import *
import numpy as np

# x = [5, 2, 9, 4, 7]
# y = [10, 5, 8, 4, 2]

# print(x,y)

# x= [5,8,10]
# y = [12,16,6]
# x2 = [6,9,11]
# y2 = [6,15,7]

# # plt.plot([1,2,4],[6,7,1])
# # plt.bar(x,y)
# # plt.scatter(x,y)

# plt.plot(x,y,color='pink',label='line1',linewidth=5)
# plt.plot(x2,y2,color='blue',label='line2',linewidth=5)

# plt.title('TEsticles')
# plt.ylabel('y-axis')
# plt.xlabel('x-axis')

# plt.legend()
# plt.savefig("mygraph.png")

# plt.show()

# x = linspace(0,10,200)
# y = sin(x)

# plt.plot(x,y)

# plt.savefig('mygraph.png')

# print(x,y)


# marks = 30 + random.rand()%100

# b = arange(0,100)

# print(filter(marks,b))

# marks = np.random.randint(30,100,100)
# averageMarks = np.average(marks)
# print(averageMarks)

# d = DataFrame({
#     'students': np.arange(1,101),
#     'marks': marks
# })

# print(d['students'])

# plt.bar(d['students'],marks)
# plt.savefig('marks.png')

# d = DataFrame({
#     'subjects': ['Maths','hindi','eng','computer','science'],
#     'percentage':[40,30,40,50,60]
# })

# plt.bar(d['subjects'],d['percentage'])

# plt.savefig('ac.png')

# elemets = np.random.uniform(100,200,10)

# print(elemets)

subjects = np.array(['Maths','hindi','eng','computer','science'])
marks = np.array([80,40,70,56,10])

plt.pie(marks,labels=subjects)
plt.savefig('stu.png')