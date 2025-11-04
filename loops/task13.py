#TODO 13= print a square of # of the size defined through input
#example: 4
####
####
####
####

size = int(input("Enter the size of the wall: "))

for i in range(size):
    for j in range(size):
        print("#", end="")
    print("")