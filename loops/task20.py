# TODO 20: take a number input from the user and then output fabonaccis sequence that many times

num = int(input("Enter the number: "))
a = 0
b = 1
count = 0
while count < num:
    print(a)
    a, b = b, a + b
    count += 1

