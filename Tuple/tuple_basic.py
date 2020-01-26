t = (1,2,3)  #this is a tuple and list is declared with square  bracket
tup = 1,2,3,4
print(t is tup)
print(id(t),'id:tup',id(tup))
t = tuple(range(5))

t = ("test",[3,4],(5,6))
print(len(t))
#rest all methods are same as list.
