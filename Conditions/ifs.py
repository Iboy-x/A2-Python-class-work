#if condition : 
# all statements in the if needs to be indented 
# when indetnation has ended the if block also ends
#else if => elif

num = int(input("Enter a number: "))
if num < 0:
    print("The number is negative")
elif num > 0:
        print("The number is positive")
else:
        print("The number is zero")
        