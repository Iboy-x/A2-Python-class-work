# task 5 : ask user for the marks and output the grade( A, B, C, D, U) 

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Your grade is A")
elif marks >= 80:
    print("Your grade is B")
elif marks >= 70:
    print("Your grade is C")
elif marks >= 60:
    print("Your grade is D")
else:
    print("Your grade is U")