# 1D array 

list = [] # empty list with no index

list.append("Zain")
list.append("Moiz")
list.append("Ali")

print(list[1])
print(len(list))

for i in range(len(list)):
    print(list[i])

list[1] = "LOL"
for name in list:
    print(name)

# arrayName = [initial value for i in range(totalindex)]
list2 = [-1 for i in range(10)]
print(list2)

list3 = [input("Enter a value: ") for i in range(3)]
print(list3)

#list 4= 