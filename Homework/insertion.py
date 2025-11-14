myList = [3, 2, 56, 99, 45, 4, 67, 98]
uBound = 8 
lBound = 0

for index in range(lBound+1, uBound):
    key = myList[index]
    place = index - 1
    if myList[place] > key:
        while place >= lBound and myList[place] > key:
            temp = myList[place + 1]
            myList[place + 1] = myList[place]
            myList[place] = temp
            place = place - 1 
        myList[ place + 1 ] = key

print(myList)