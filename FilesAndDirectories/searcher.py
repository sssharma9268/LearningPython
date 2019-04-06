import os

def search(key):
    #here we will list all the files in current directory and one by one check all files for perticular key
    for file in os.listdir(os.getcwd()):
        try:
            f = open(file)
            for line in f:
                if key in line:
                    f.close()
                    return True, file
        except:
            pass
    return False, None


key = input("Enter the search key: ")

isFound, filename = search(key)
print("Found",isFound)
print("Filename",filename)