#TODO 26: Take input from the user and check if the paranthess are correct () 

inp = input("Enter the string: ")

openP = 0 
closeP = 0 

for i in range(len(inp)):
    if inp[i] == "(":
        openP += 1
    if inp[i] == ")":
        closeP += 1

if closeP == openP:
    print("perfect Mate")
else:
    print("KYS YOU RETARDED CANT EVEN PLACE PERFECT () ")