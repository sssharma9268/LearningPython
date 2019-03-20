animals = ["lion","tiger","dog"]

i = 0

while i < len(animals):
    print(animals[i])
    i+=1

n = [1,2,3,[4,5],[6,[7,8]]]

#ways to access list elements

print(n[3][0])
print(n[4][1][0])

a = list(range(0,9))
print(a[:]) #prints the whole list
print(a[2:])  #prints from index 2 to rest
print(a[3:6]) #prints elements between index 3 and 6
print(a[:7]) #prints from starting till 7

del a

a =[1,2]
b=a+["x","y"]

c = ["x","y"]*4



