#1.Write a program which will find factors of given number and find whether the factor is even or odd.
# Hint: Use Loop with if-else statements
# def print_factors(x):
#    print("The factors of",x,"are:")
#    for i in range(1, x + 1):
#        if x % i == 0:
#            if i %2 ==0:
#                print(str(i)+"-even")
#            else:
#                print(str(i)+"-odd")
# num = 250
# print_factors(num)

# 2.Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.

# import sys
#
# mystr = str(input())
# mylist=mystr.split(" ",mystr.count(" "))
# mylist = sorted(mylist)
# for i in range(0,len(mylist)):
#     print(mylist[i])


# 3.Write a program, whichwill find all the numbers between 1000 and 3000 (both included)
# such that each digit of a number is an even number.
# The numbers obtained should be printed in a comma separated sequence on a single line.
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
# Divide each digit with 2 and verify is it even or not.
# myList = []
# flag = 0
# for i in range(1000,3001):
#     flag = 0
#     n=i
#
#     while(n>0):
#         digit = n%10
#         n = n//10
#         if digit%2 != 0:
#             flag = 1
#
#     if(flag==0):
#         myList.append(i)
#
# print(myList)


# 4.Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose if the entered string is: Python0325Then the output will be:LETTERS: 6DIGITS:4
# Hint: Use built-in functions of string.


# s = input()
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters: ", l)
# print("Digits: ", d)


# 5.Design a code which will find the given number is Palindrome number or not.Hint: Use built-in functions of string.

number = input()

if(number==number[::-1]):
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")