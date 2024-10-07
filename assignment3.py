def count_digits(s):
    return len([char for char in s if char.isdigit()])

s=input("Enter a number: ")
result=count_digits(s)
print("Number of digits in", s, "is", result)
