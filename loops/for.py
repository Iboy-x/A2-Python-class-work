#LOOPS
        #1) for loop
            #range(start, end, iteration):
            #range(start, end): iteration = +1
            #range(end): start = 0, iteration = +1
            #for variableName in range():
            #for loop ends before the last value in range()

print("LOOP 1")
for i in range(2,7,1):
    print(i)
    
print("LOOP 2")
for i in range(2,10,2):
    print(i)

print("LOOP 3")
for i in range(10,3,-1):
    print(i)

print("LOOP 4")
for i in range(2,7):
    print(i)

print("LOOP 5")
for i in range(7,2):
    print(i)

print("LOOP 6")
for i in range(5):
    print(i)

print("LOOP 7")
for i in [1,13,6,9]:  #list can have names, numbers etc will be printed one by one
    print(i, end= "")   #without space " " with space, can write letters or sum' else asw

#print() changes line by default but we can change it using end= function