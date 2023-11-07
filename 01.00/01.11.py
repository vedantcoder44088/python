# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data: c. -> [1, 5, 8, 3]: True -1 -> [1, 5, 8, 3]: False

def is_value_contained(value, group):
    return value in group
def main():
    group = [1,5,8,3]
    value1 = 'c'
    result1 = is_value_contained(value1, group)
    value2 = -1
    result2 = is_value_contained(value2, group)
    print(result1)
    print(result2)
if __name__ == '__main__':
    main()