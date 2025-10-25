# task 8: Ask user for 5 inputs and outut the largest and smallest

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))

# Finding the largest number
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4
if num5 > largest:
    largest = num5

# Finding the smallest number
smallest = num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num4 < smallest:
    smallest = num4
if num5 < smallest:
    smallest = num5

print("Largest number is:", largest)
print("Smallest number is:", smallest)