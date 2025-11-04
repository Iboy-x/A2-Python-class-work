#TODO: 12: print a reverse staircase of # of the size defined through input
#example: 4
####
###
##
#

size = int(input("Enter the size of staircase: "))

for i in range( size, 0, -1):
    for j in range(i, 0, -1):
        print("#", end="")
    print(" ")