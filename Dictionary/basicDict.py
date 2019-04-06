d = {}
d = {1:"x",2:"y"}
d = {"test":3,2:["x",4]}
d = dict({1:2,"x":"y","test":[5,6]})

#for i in d:  By default prints values
#    print(d[i])

#for i in d.values():  prints only values
#    print(i)

#d.get("x")  these are two ways to get values using keys
#d["x"]  get method will return null if key is not present while this will return key error

for i in d.keys(): #traverses through only keys and prints it
    print(i)

d = {'name':"Sumit",'lastname':"Sharma",'age':25}

length = len(d)
d.update({"age":20})
d.pop()  #by default pops the last pair, else u can specify the key u want to pop

d = {x:x*x for x in range(10) } #create a dict whose values are squares of their keys

d = {x:x*x for x in range(10) if x % 2 == 0} # does same as above but only considers even no's as pairs