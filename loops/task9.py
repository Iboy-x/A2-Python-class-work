# TODO: Ask user for a number and output each digit as a word
#example: 123
# one two three

num = int(input("Enter a number: "))

for digit in str(num):
    if digit == '0':
        print("Zero ", end="")
    if digit == '1':
        print("One ", end="")
    if digit == '2':
        print("two ", end="")
    if digit == '3':
        print("three ", end="")
    if digit == '4':
        print("four ", end="")
    if digit == '5':
        print("five ", end="")
    if digit == '6':
        print("six ", end="")
    if digit == '7':
        print("seven ", end="")
    if digit == '8':
        print("eight ", end="")
    if digit == '9':
        print("nine ", end="")