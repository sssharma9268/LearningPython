l = [2,5,2]
t = (1,2,3,'hello',l)
l[0]=1
l=[4,6,6]
l[0]=1
print(t)


l=[10,15,3,7]
k=17
var = []

for i in range(0, len(l)-1):
    for j in range(i+1, len(l)):
        a = l[i]+l[j]
        if a == k:
            var.append(str(l[i])+"-"+str(l[j]))

print(var)