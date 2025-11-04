# TODO: 10 = use the loop to print a formatted multiplication table from 1 to 10
#for a value input
# 1 X 5 = 5

num = int(input("Enter a number: "))

for i in range (1,11):
    print(num, "x", i, "=", num*i)