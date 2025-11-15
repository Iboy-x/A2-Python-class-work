# TODO 25: Take input from the user and shuffle them into one

inp1 = input("Enter the first string: ")
inp2 = input("Enter the second string: ")

if len(inp1) > len(inp2):
    lim = len(inp1)
else:
    lim = len(inp2)

for i in range(lim):
    if i <  len(inp1):
        print(inp1[i], end="")
    if i < len(inp2) : 
        print(inp2[i], end="")
   