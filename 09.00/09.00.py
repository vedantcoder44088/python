import re

# 1) Search if a string starts with "The " and ends with "Indus"
string1 = "The river flows into Indus"
match1 = re.search(r'^The .*Indus$', string1)
print("1)", match1)

# 2) Find a match where the string contains a whitespace character
string2 = "This is a sample string."
match2 = re.search(r'\s', string2)
print("2)", match2)

# 3) Match a string that has an 'a' followed by three 'b's
string3 = "abbb"
match3 = re.search(r'abbb', string3)
print("3)", match3)

# 4) Find words or strings having three characters and with 'm' as the first character
string4 = "mat sun moon"
match4 = re.findall(r'\bm\w{2}\b', string4)
print("4)", match4)

# 5) Retrieve all words starting with "a"
string5 = "apple and orange are fruits"
match5 = re.findall(r'\ba\w+', string5)
print("5)", match5)

# 6) Retrieve all words starting with a numeric digit
string6 = "5apples and 3oranges"
match6 = re.findall(r'\b\d\w+', string6)
print("6)", match6)

# 7) Retrieve all words having 5-character length
string7 = "apple orange mango"
match7 = re.findall(r'\b\w{5}\b', string7)
print("7)", match7)

# 8) Retrieve all words with 3, 4, or 5 character length
string8 = "car bus train bike"
match8 = re.findall(r'\b\w{3,5}\b', string8)
print("8)", match8)

# 9) Retrieve all single digits from a string
string9 = "Sample 123 string 456 with 7 digits."
match9 = re.findall(r'\b\d\b', string9)
print("9)", match9)

# 10) Retrieve the last word from the string
string10 = "This is the last word"
match10 = re.findall(r'\b\w+\b$', string10)
print("10)", match10)

# 11) Retrieve all words starting with 'an' or 'ak'
string11 = "an apple and ak orange"
match11 = re.findall(r'\b(?:an|ak)\w+', string11)
print("11)", match11)

# 12) Retrieve DOB from the string
string12 = "Date of Birth: 1990-01-01"
match12 = re.findall(r'\d{4}-\d{2}-\d{2}', string12)
print("12)", match12)
