def displayBoard(myArr):
    for row in range(len(myArr)):
        for col in range(len(myArr[row])):
            print(myArr[row][col], end=" ")
        print()

Board = [ [ 0, 0, 0, 0, 0, 0, 0],
          [ 0, 0, 0, 0, 0, 0, 0],
          [ 0, 0, 0, 0, 0, 0, 0],
          [ 0, 0, 0, 0, 0, 0, 0],
          [ 0, 0, 0, 0, 0, 0, 0],
          [ 0, 0, 0, 0, 0, 0, 0]   ]

print(len(Board)) #number of rows
print(len(Board[0])) # number of COLS
Board[0][0] = 1 #arrayName[row][col] = value
Board[2][4] = 5
print(Board[0][0]) 

displayBoard(Board)

#arrayName = [ [ initial value for col in range(totalcols)] for row in range(totalRows) ]
table = [["X" for col in range(3)] for row in range(4)]
displayBoard(table)

