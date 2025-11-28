# TODO 32: for a game that runs for 3 round,  throw 2 dices and output the 7 ups 7 downs or luck 7 for 


from random import randint

for i in range(3):
    num1 = randint(1,6)
    num2 = randint(1,6)
    x = int(num1 + num2) 
    
    if x == 7: 
        print("Lucky 7 ")
    elif x < 7:
        print("7 down ")
    else: 
        print("7 up")
