import csv


with open("C:/Users/sush0717/Desktop/info.txt","r") as f:
   reader = list(csv.reader(f,delimiter=' '))

reader = [i for i in reader if i]

targetIndex=0
for i in range(2,len(reader)):
    reader[i] = list(reader[i])
    if 'Active' in reader[i]:
        targetIndex = reader[i].index('Active')+1
    elif 'Standby' in reader[i]:
        targetIndex = reader[i].index('Standby')+1

    if 'CACHE=CACHE01' in reader[i]:
        continue
    if 'CACHE=SCACHE01' in reader[i]:
        continue
    elif 'DG=1' in reader[i]:
        continue
    else:
        reader[i].insert(targetIndex,'DUMMY')


for i in range(0,len(reader)):
    reader[i]=list(reader[i])
    reader[i] = [j for j in reader[i] if j]

names=[]
host=[]
admin=[]
presence=[]
readiness=[]

nameIndex=reader[0].index('Name')
hostIndex=reader[0].index('Host')
adminIndex=reader[0].index('Admin')
presenceIndex=reader[0].index('Presence')
readinessIndex=reader[0].index('Readiness')

del reader[0:2]

for row in reader:
    names.append(row[nameIndex])
    host.append(row[hostIndex])
    admin.append(row[adminIndex])
    presence.append(row[presenceIndex])
    readiness.append(row[readinessIndex])




uniqueHost=[]

for x in host:
    if x not in uniqueHost:
        uniqueHost.append(x)

print("Unique Host-->",uniqueHost)

count=0
for uni in uniqueHost:
    for nm in names:
        if nm == uni:
            rIndex = names.index(nm)
            count+=1
            print("Name-->"+nm+" "+"Readiness-->"+readiness[rIndex])

print("Readiness Count-->",str(count))

# print(names)
# print(uniqueHost)
# print(admin)
# print(presence)
# print(readiness)







