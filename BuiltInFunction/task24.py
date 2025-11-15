#TODO 24: take an input from the user and check if it palindrome

x = input("Enter the string: ")
revered = x[::-1]
if x == revered:
    print("The string is a palindrome")
else:
    print("Not a palindrome")