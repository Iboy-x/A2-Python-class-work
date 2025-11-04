#TODO 15: output a pyramid of size defined through input of the symbol defined through input
#example: size = 4, symbol = #
     #
   ###
 #####
#######

# there will be size - 1 space in the first one and then size - 2 spac in carry on
# the pattern for brick in each line is (n*2-1)

# METHOD 1 :
size = int(input("Enter the size of the pyramid: "))

for i in range(size + 1):
    for j in range(size - i):
        print(" ", end="")
    print("#"*(i*2-1))
  

# METHOD 2 : ALTERNATIVE METHOD :)

for i in range(size + 1):
    for j in range(size - i):
        print(" ", end="")
    for y in range(i*2 -1):
        print("#", end="")
    print(" ")