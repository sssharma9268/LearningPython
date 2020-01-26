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


str = "abcd"
n=len(str)
def all_substrings(str,n):
    res = [ str[i:j] for i in range(n) for j in range(i+1,n)]
    print(res)

all_substrings(str,n)


