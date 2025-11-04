#TODO 16: output fish of size defined through input of the symbol defined through input
#example: size = 4, symbol = #

      # 
   ####
  #####
 #######
  #####
   ###
     #
   ###
 #####
#######
size = int(input("enter the size of fish: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for y in range(i*2 -1):
        print("#", end="")
    print()

for i in range(size -1 , 0, -1):
    for j in range(size - i):
        print(" ", end="")
    for y in range(i*2 -1):
        print("#", end="")
    print()

for i in range(2, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for y in range(i*2 -1):
        print("#", end="")
    print()