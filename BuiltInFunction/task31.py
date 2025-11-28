# TODO 31: throw a dice and output after how many thows does a person gets 1 

from random import randint
num = randint(1,6)
tries = 1
while num != 1 :
    num = randint(1,6)
    tries += 1

print ("got 1 in:", tries, "tries")
