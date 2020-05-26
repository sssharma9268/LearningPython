# d = {}
# d = {1:"x",2:"y"}
# d = {"test":3,2:["x",4]}
# d = dict({1:2,"x":"y","test":[5,6]})
#
# #for i in d:  By default prints values
# #    print(d[i])
#
# #for i in d.values():  prints only values
# #    print(i)
#
# #d.get("x")  these are two ways to get values using keys
# #d["x"]  get method will return null if key is not present while this will return key error
#
# for i in d.keys(): #traverses through only keys and prints it
#     print(i)
#
# d = {'name':"Sumit",'lastname':"Sharma",'age':25}
#
# length = len(d)
# d.update({"age":20})
# #d.pop()  #by default pops the last pair, else u can specify the key u want to pop
#
# d = {x:x*x for x in range(10) } #create a dict whose values are squares of their keys
# print(d)
# d = {x:x*x for x in range(10) if x % 2 == 0} # does same as above but only considers even no's as pairs
# print(d)

devicenames=["lamp","lamp","tv","lamp"]

def deviceNamesSystem(devicenames):
    # Write your code here
    # setNames=set(devicenames)
    # dictOfNames = dict.fromkeys(setNames,0)
    # uniqueDict=dict.fromkeys(setNames,0)
    uniqueNames=[]
    dictNames={}
    for n in devicenames:
        if n not in dictNames:
            uniqueNames.append(n)
            dictNames[n]=1
        else:
            uniqueNames.append(n+str(dictNames[n]))
            dictNames[n]+=1

    for n in uniqueNames:
        print(n)

    # Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def isValid(S):
    char_map = Counter(S)
    print(char_map)
    char_occurence_map = Counter(char_map.values())
    print(char_occurence_map)
    if len(char_occurence_map) == 1:
        return True

    if len(char_occurence_map) == 2:
        for v in char_occurence_map.values():
            if v == 1:
                return True

    return False

S = "abcccf"
if isValid(S):
    print("YES")
else:
    print("NO")




    # for name in devicenames:
    #     dictOfNames[name]+=1
    #     if dictOfNames[name]>1:
    #         uniqueNames.append(name+str(dictOfNames[name]-1))
    #
    # for k in uniqueDict.keys():
    #     print(k)

    # for names in devicenames:
    #     dictOfNames[names]+=1
    #
    # uniqueNames.append(devicenames[0])

    # for i in range(1,len(devicenames)):
    #     if devicenames[i] in uniqueNames:
    #         k=dictOfNames[devicenames[i]]-1
    #         devicenamesModify=devicenames[i]+str(dictOfNames[devicenames[i]]-k)
    #         dictOfNames[devicenames[i]]+=1
    #         uniqueNames.append(devicenamesModify)
    #     else:
    #         uniqueNames.append(devicenames[i])



    # for key,value in dictOfNames.items():
    #     print(key,value)
    # for strs in uniqueNames:
    #     print(strs)





# strs=
# deviceNamesSystem(devicenames)
# for s in strs:
#     print(s)