#TODO 17: take an input and output if the number is prime

# prime numbers come only in theri own and 1 ka table

num = int(input("Enter a number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime == True:
    print("the number is prime")
else:
    print("not a prime number")