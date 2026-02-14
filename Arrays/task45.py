# Make three array for 10 students, one for the math marks, 
# one for the CS marks and one for physics marks. Take three input of all marks

mathsMarks = [int(input("Enter maths marks : ")) for i in range(9)]
CsMarks = [int(input("Enter CS marks : ")) for i in range(9)]
phyMarks = [int(input("Enter physics marks : ")) for i in range(9)]

print(mathsMarks)
print(CsMarks)
print(phyMarks)