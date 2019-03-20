letters = "abcdefgh"
letters = " ".join(letters)
print(letters)
letters = "abcdefgh"
letters = "|".join(letters)
print(letters)

message = """ First Line
Second Line
Third Line
"""

print(message)
message = message.splitlines()
print(message)


print("{0} {1} {2}".format("a","b","c"))
print("{1} {2} {0}".format("a","b","c"))
print("{1} {1} {2} {0}".format("a","b","c"))
print("{1} {1} {2} {0}".format(*"abc"))
print("{name} and {number}".format(name="Sumit",number="123"))

