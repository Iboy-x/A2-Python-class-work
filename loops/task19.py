# TODO 19: ask user for the input until armstrong number is found


armstrong = False


while armstrong != True:
    num = int(input("Enter the number: "))

    digit1 = num % 10
    digit3 = (num // 100) 
    digit2 = (num // 10) - digit3*10

    if digit1**3 + digit2**3 + digit3**3 == num:
        armstrong = True
        print("the number is armstorng")

