from matplotlib import pyplot as plt
from numpy import *

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

x = linspace(0,10,200)
y = sin(x)

plt.plot(x,y)

plt.savefig('mygraph.png')

# print(x,y)
