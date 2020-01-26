# 1.A Robot moves in a Plane starting from the origin point (0,0).
# The robot can move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after directions are steps.  Write a program to compute the distance current position after sequence of movements.
# Hint: Use math module.
# import math
#
# x, y = 0, 0
#
# while True:
#     step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")
#
#     if step == "":
#         break
#
#     else:
#         step = step.split(" ")
#
#         if step[0] == "UP":
#             y = y + int(step[1])
#         elif step[0] == "DOWN":
#             y = y - int(step[1])
#         elif step[0] == "LEFT":
#             x = x - int(step[1])
#         elif step[0] == "RIGHT":
#             x = x + int(step[1])
#
# c = math.sqrt(x**2 + y**2)
#
# print("Distance:", c)

# 2.Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
# Hint:
# Use if/elif to deal with conditions.

# data = ["mumbai","pune","delhi","banglore","hyderabad","gurugram","noida"]
#
# dataTobeSearched = "pune"
#
# if dataTobeSearched in data:
#     print("Found data: "+dataTobeSearched.upper()+" at index: "+str(data.index(dataTobeSearched)))
# else:
#     print("The data is not present in the list")

# 3.Weather forecasting organization wants to show is it day or night.
# So, write a program for such organization to find whether is it dark outside or not.
# Hint: Use time module.
# import time
# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))
#
# mytime = time.localtime()
#
# if mytime.tm_hour < 6 or mytime.tm_hour > 18:
#     print ('It is night-time')
# else:
#     print ('It is day-time')

# 4.Write a program to find distance
# between two locations when their latitude and longitudes are given.
# Hint: Use math module.
# from math import radians, sin, cos, acos
#
# print("Input coordinates of two points:")
# slat = radians(float(input("Starting latitude: ")))
# slon = radians(float(input("Ending longitude: ")))
# elat = radians(float(input("Starting latitude: ")))
# elon = radians(float(input("Ending longitude: ")))
#
# dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
# print("The distance is %.2fkm." % dist)


# 5.Design a software for bank system. There should be options like cash withdraw, cash credit and change password.
# According to user input, the software should provide required output.Hint: Use if else statements and functions.
# print("************Welcome**********\n")
# print("Please enter the chose one of the following options\n")
# print("1.Cash Withdraw\n2.Cash Credit\n3.Change Password\nChose option 1 2 or 3")
# input = input()
# if int(input) == 1:
#     print("Thank you for chosing Cash Withdraw")
# elif int(input) == 2:
#     print("Thank you for chosing Cash Credit")
# elif int(input) == 3:
#     print("Thank you for chosing change password")


# 6.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
# numbers =[]
# for i in range(2000,3201):
#     if (i%7 ==  0) and (i%5!=0):
#         numbers.append(i)
#
# print(numbers)

# 7. Write a program which can compute the factorial of a given numbers. Use recursion to find it.
# Hint: Suppose the following input is supplied to the program:8 Then, the output should be: 40320

# def factorial(number):
#     if number ==1:
#         return 1
#     else:
#         return number*factorial(number-1)
#
# print(factorial(8))

# 8.Write a program that calculates and prints the value according to the given formula:Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D  is  the  variable  whose  values  should  be  input  to  your  program  in  a  comma-separated sequence.
# Example:Let  us  assume  the  following  comma  separated  input  sequence  is  given  to  the program:100,150,180
# The output of the program should be:18,22,24
# import math
# C = 50
# H = 30
# input = input()
# mylist = input.split(",")
#
# result = []
# for i in mylist:
#     D = int(i)
#     value = math.sqrt((2*C*D)/H)
#     result.append(int(value))
#
# print(result)


# 9.Write a program which takes 2 digits, X,Y as input and generates a 2 -dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡-Y-
# 1.Example:Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# x, y = input().split(",")
# a = []
# for i in range(int(x)):
#     inlist = []
#     for j in range(int(y)):
#         inlist.append(i*j)
#     a.append(inlist)
#
# print(a)

# 10.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence
# after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be:bag,hello,without,world
# mystr = input().split(",")
# print(sorted(mystr))

# 11.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence
# capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# print(input().upper())

# 12.Write a program that accepts a sequence of whitespace separated words as input and   prints   the   words   after
# removing   all duplicate   words   and   sorting   them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# mystr = sorted(set(input().split(" ")))
#
# for str in mystr:
#     print(str+" ")


# 13.Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary numbers  as  its  input  and
# then  check  whether  they  are  divisible  by  5  or  not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# b_num = list(input().split(","))
#
# def decimalNumber(b_num):
#     value = 0
#     b_num = list(b_num)
#     for i in range(len(b_num)):
#         digit = b_num.pop()
#         if digit == '1':
#             value = value + pow(2, i)
#     return value
#
# for i in range(len(b_num)):
#
#     if (decimalNumber(b_num[i])%5==0):
#         print(b_num[i]+" ")



# 14.Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# mystr = input()
# countUpper =0
# countLower = 0
# for i in mystr:
#     if i.isupper():
#         countUpper +=1
#     elif i.islower():
#         countLower +=1
#     else:
#         continue
#
# print("UPPER CASE "+str(countUpper))
# print("LOWER CASE "+str(countLower))

# 15.Give example of fsum and sum function of math library
import math
b = [10, 20, 30, 40, 50]
c = [10, 20, 30.30, 40, 50.0]

print("sum(b): ", sum(b))
print("fsum(c): ", math.fsum(c))

