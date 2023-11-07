
ends_with_character = lambda string, char: string[-1] == char

test_string = "Hello"
test_character = "o"

result = ends_with_character(test_string, test_character)
print(f"Does the string '{test_string}' end with the character '{test_character}'? : {result}")
