import os
import sys

print(os.getcwd())
#os.mkdir("test") create a directory name test
#os.listdir()  list of directory present in current path
#os.rmdir("test") removes the directory

f = open("test.txt","w")  #if file not present creates it and opens it in write mode, if it is in read mode it gives exception if file is not present
f.write("First line\n")
f.write("Second line\n")
f.close()
f = open("test.txt")
print(f.read(5)) #no size specified, reads the whole file text
print(f.tell()) #points the file cursor
print(f.seek(0)) #change the file cursor where u specify
print(f.readline())
f.seek(0)
print(f.readlines()) #reads all line and returns a list of lines
f.close()

with open("test.txt",'a') as f: #here a is to append
    f.write("Sumit\n")
    f.write("Sharma\n")

f = open("test.txt")
for line in f:
    print(line)

#Exception Handling

try:
    f = open("test2.txt")
    var = 5/0
except FileNotFoundError:
    print("Error",sys.exc_info()[0]) #here sys module is used to know the type of error, stores the tuple of information regarding the current stack frame.
    #here at except u can catch a specific exception like except FileNotFoundError
except ZeroDivisionError:
    print("Divide by zero Exception")
finally:
    f.close()
