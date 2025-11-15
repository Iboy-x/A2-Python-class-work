#TODO 21: take an input from the user and output string of the increasing size

x = input("Enter the string: ")

for i in range(len(x) + 1): 
    print(x[:i])