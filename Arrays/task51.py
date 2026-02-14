# TODO 51: Make a two player tic tac toe 

def changeToken(token):
    if token == "o":
        return "x"
    if token == "x":
        return "o"

ttt = [["-" for col in range(3)] for row in range(3)]

win = False
turn = 0 
token = "o"
while not win and turn < 9:  
    token = changeToken(token)