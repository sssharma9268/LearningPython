import numpy as np

a  = np.array([[1,2,3],[4,5,6]])
#print(a)

b = np.arange(0,100)
# print(b)

c = np.zeros([5,15])
d = np.ones([10,10])
vector = np.linspace(0,20,5)
# print(vector)

e = np.zeros(8)
#2 rows and 2 columns of 2 arrays..product of dimensions will always be equal to original size..2*2*2=8
e = e.reshape((2,2,2))
#ravel flattens the multidimensional array into sinlge line array
# print(e.ravel())

f = np.arange(20)
arr_slice = slice(1,10,2)
# print(f[arr_slice])
g = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(g.shape)
# print(g.ndim)
# print(g.itemsize)
# print(g[0:3,:3])

#Create an unintialized array with random values
x = np.empty([3,5],dtype=int)
print(x)

#Read and write to file using np
# arr = np.loadtxt('file.txt')
arr = np.arange(10,101)
np.savetxt('file.txt',arr)
arrcsv = np.array([[1,2,3],[4,5,6]])
np.savetxt('newfile.csv', arrcsv, delimiter=",")