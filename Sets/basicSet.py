s = {1,2,3,4}
#it will only consider uniques values and remove the duplicate values
s = {1,1,1,2,2,2,2,3,3,3,3,4,4,4,4}
s = {"x",2,(3,4)} #allows only tuple and list as list is mutable
s=set([1,2,3,4])  #but here using set method u can use list to create a set
s = set("Hello")

#traversing a set
for i in s:
    print(i)

#set methods
s = {1,2,3,4}
s.update([9,10],{11,2,34})
s.discard(2) #does not raises and error if an item is not present
s.remove(34) #raises an error if an item does not present in the set
s.pop()
sorted(s)
X=set(range(0,7))
Y=set(range(3,10))
print(X.union(Y))
print(X.intersection(Y)) #only which are common in both
print(X.difference(Y))#elements in X which are not common
print(X.symmetric_difference(Y))#elements from both which are not common with one another





