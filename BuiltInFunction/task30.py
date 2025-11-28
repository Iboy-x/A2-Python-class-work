# TODO 30: throw a dice 100 times and output avg of all the dice thrown 

from random import randint
sum = 0 
for i in range(99):
    sum += int(randint(1,6))

avg = sum / 100

print (avg)