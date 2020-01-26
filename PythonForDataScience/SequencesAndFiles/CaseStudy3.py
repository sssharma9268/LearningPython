# Approach to Solve
# You have to use fundamentals of Python taught in module
# 1
# 1.Read the input from command line –Reference ID
# 2.Check for validity –it should be 12 digits and allows on number and
# Alphabet
# 3.Encrypt the Reference ID and print it for reference
#
# Enhancements for code
# You can try these enhancements in code
# 1.Allow some special characters in ReferenceID
# 2.Give the option for decryption to user
import re
referenceId = input("Enter the 12 digit alpha-numberic referenceId:  ")

def authenticate(referenceId):
    pattern = re.compile('^(?=.*[a-z])(?=.*\d)[A-Za-z\d@$!%*?&]{12}$')

    if pattern.search(referenceId)!=None:
        print("The entered reference id accepted")
        encoded = referenceId.encode('utf-8')
        print(encoded)
        print(encoded.decode('utf-8'))

    else:
        print("The refernce id does not match the criteria of 12 digits alpha-numberic")
        referenceId = input("Please enter the reference id again: ")
        authenticate(referenceId)

authenticate(referenceId)


