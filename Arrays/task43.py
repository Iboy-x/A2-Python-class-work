# TODO 43: keep taking students names as input from user until user enters 0 0
# output total names that were input

x = ""
names = []
while x != "0" :
    names.append(x)
    x = input("Enter the name of student: ")

print(names[1::])
    
