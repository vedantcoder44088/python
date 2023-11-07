# Practical based on Strings (Length finding,change specific character, palindrome,concatenation)

string = "Hello, World!"
print("Length Of String: ", len(string))
index = 4
new_char = 'x'
new_string = string[:index] + new_char + string[index+1:]
print("New String:", new_string)

def is_palindrome(s):
    return s == s[::-1]
string = "radar"
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")