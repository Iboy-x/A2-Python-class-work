mylist = [4, 2, 8, 17, 9, 3, 7, 90]

item = int(input("Please enter a number between 1 and 100: "))

found = False

for index in range(8):
    if mylist[index] == item:
        found = True
    

if found:
    print("item found")
else:
    print("not found")