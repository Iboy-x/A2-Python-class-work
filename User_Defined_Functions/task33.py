# TODO 33: Creat a funtion that takes 2 numbers as a parameter and return the larger value0

def largerValue(num1, num2):
    if num1 > num2:
        return num1, "First number is larger"
    else:
        return num2, 'Sec numbers is larger'
    

ans, thisans = largerValue(5,6)
print(ans, thisans)
    