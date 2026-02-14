# TODO 46: Use the arrays from Task 45 and output the highest and lowest marks of each subject, average marks for each student, average marks for the class

mathMarks = [76, 90, 89, 98, 78, 98, 95, 85, 70]
CsMarks = [87, 78, 90, 99, 98, 97, 95, 56, 78]
PhyMarks = [90, 90, 78, 68, 57, 47, 74, 79, 90]

Lmaths = min(mathMarks)
Hmaths = max(mathMarks)
Lcs = min(CsMarks)
HCs = max(CsMarks)
Lphy = min(PhyMarks)
Hphy = max(PhyMarks)

avg = []
for i in range(9):
    average = (mathMarks[i] + CsMarks[i] + PhyMarks[i] )/3
    avg.append(average)
  

print("highest marks are: ", Hmaths, HCs, Hphy)
print("Lowest marks are : ", Lmaths, Lcs, Lphy)
print("Avg marks for each student is: ", avg)