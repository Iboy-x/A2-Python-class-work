#TODO 14: ask user for total students in class, take input for marks for all students
#output the average, highest and lowest marks

StNum = int(input("Enter the number of students: "))
total = 0

mark = int(input("Enter marks for student 1 : "))
highest = mark
lowest = mark
total += mark
for i in range(1, StNum):
    mark = int(input("Enter marks for student: "))
    total += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    
avg = total / StNum

print("The average is: ", avg )
print("Highest is: ", highest)
print("Lowest is: ", lowest)
    
