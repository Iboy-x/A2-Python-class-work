# task 4 : ask user for age and users sibling age and output who is older 

userAge = int(input("Enter your age: ")) 
sibAge = int(input("Enter your sibling age: "))

if userAge > sibAge: 
    print("You are older than your sibling")
elif sibAge > userAge:
    print("Your sibling is older than you")
else:
    print("You and your sibling are of the same age")