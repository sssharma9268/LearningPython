n = list(range(10))

max = max(n)
min = min(n)

n = n.append(1)

count = n.count(1)

index = n.index(1)

n.insert(1,100)

n.extend("x","y")

n.pop()  #by default pops the last element

n.pop(1)  #pops the specified element

n.remove("x")

n.reverse()
n.sort()


#various ways of creating a list

#1. n = [i for i in range(5)]
#2. n = [i*i for i in range(5)]
#3. n = [i+2 for i in range(10) if i>7]
#4. n = [x+y for x in [1,3] for y in [6,9]]
#5. n = [x+y for x in [1,3] if x>1 for y in [6,9] if y>7]
#6. n = [x+y for x in [1,3] for y in [6,9] if x>1 and y>7]