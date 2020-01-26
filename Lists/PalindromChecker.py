#1st Method to check
def is_palindrom(word):
    if len(word) <=1:
        return True
    elif word[0]!=word[-1]:
        return False
    else:
        return is_palindrom(word[1:-1])

#2nd method to check
def is_palindrome_easy(word):
    return word == word[::-1]   #word[::-1] is short-cut way to reverse a list

print("Palindrome Words")
word = input("Word: ")
print("Is Palindrome: ",is_palindrome_easy(word))

word1 = "Hello"
print(word1)
print(word1[::-1])