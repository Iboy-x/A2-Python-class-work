#TODO: 11= print a staircase of # of the size defined through input
#example: 4
#
##
###
####

size = int(input("Enter size for staircase: "))

for i in range (1, size + 1):
    for j in range(0, i):
        print("#", end="")
    print(" ")