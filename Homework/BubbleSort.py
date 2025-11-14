#TODO: bubble sort, linear search, insertion sort, binary search, linked list

# TODO BUBBLE SORT

myList = [1, 4, 6, 98, 56,90, 9, 67]
top =  8
swap = True

ubound = 8
Lbound = 0 

while swap or top > 0:
    swap = False
    for index in range(top - 1):
        if myList[index] > myList[index + 1 ]:
            temp = myList[index]
            myList[index] = myList[index + 1]
            myList[index + 1] = temp
            swap = True
    top -= 1
    

print(myList)
