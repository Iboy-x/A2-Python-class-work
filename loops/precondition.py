#pre-condition loop
#while condition:
#the loop runs when the condition is true
#the loop ends when the condition is false

num = int(input("Enter an even number: "))
while num % 2 != 0:
    num = int(input("Enter an even number: "))
print("The number is", num)