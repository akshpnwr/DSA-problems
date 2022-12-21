from pandas import *
from numpy import *

# d = DataFrame({
#     "Name": ['akash','tanishka'],
#     'age':[22,56]
# })

# print(d)

# s = Series(arange(10),dtype=float64)
# print(s)

# d = DataFrame({
#     'coffee':[2,6],
#     'chai':[5,1]
# }, index=['tanishka','akash'])

# print(d)

# stu = [(1,'akash','dun'),(2,'swapnil','sahran'),(3,'tanishka','dun')]

# d = DataFrame(stu,columns=['id','name','city'],index=['a','b','c'])


# print(d)
# # del d['id']

# print(d.T)

# print(d.head(1))
# print(d.tail(-1))
# 

# print(d.loc['a'])
# cd = d.loc[:1:-1,'name':]
# print(cd)
# print(type(d['name']))

# print(d.iloc[[1,2],[0,2]])


# csv = read_csv('purchases.csv',index_col=0)
# print(csv)

# xl = read_excel('purchases.xlsx')
# print(xl)

# xl.to_excel('write.xlsx',sheet_name='sheet1')

# names = array(['akash','tanishka','sawap'])
# ages = array([22,23,42])

# ndata = [names,ages]
# nd = DataFrame(data=ndata, index=['row1','row2'], columns=['col1','col2','col3'])

# print(nd)

# print(nd.sample(1))
# print(nd['col1'].value_counts())
# print(nd.size)

# s = Series(arange(5),dtype=int32)

# print(s.describe())

d = DataFrame({})

# a = read_csv('data.csv')

# clean_csv

print(d)

d.to_csv('data.csv')

a = read_csv('data.csv')

print(a)