mylist = [2, 3, 4, 45, 56, 67, 98, 99]

item = int(input("Please enter a number between 1 and 100: "))

found = False
lbound = 0 
Ubound = 8

while not found and lbound != Ubound:
    index = int((Ubound + lbound)/ 2)
    if item == mylist[index]:
        found = True
    if item > mylist[index]:
        lbound = index + 1
    if item < mylist[index]:
        Ubound = index - 1 

if found:
    print("Item found")
else:
    print("Item not found")
