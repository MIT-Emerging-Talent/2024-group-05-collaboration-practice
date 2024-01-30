#Add string numbers
''' designed to add two numbers represented as strings. The tests cover scenarios such as adding single and double-digit integers,
large numbers, floating-point numbers, and combinations of these cases'''
#Given two strings of numbers, add the numbers together and return the result as a string.
#Example:
#Input: "123", "456"


def add_string_numbers(num1, num2):
    # Fill this in.
    return str(int(num1) + int(num2))

if __name__ == "__main__":  
    print(add_string_numbers("123", "456"))
    # 579
    print(add_string_numbers("123", "456"))
    # 579
    print(add_string_numbers("123", "456"))



