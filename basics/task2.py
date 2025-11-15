'''
Take your sibming age as input and out put 
how old they will be when you turn 50
'''

sibling_age = int(input("Enter your sibling's age: "))
your_age = int(input("Enter your age: "))
age_difference = your_age - sibling_age
print("Your sibling will be", sibling_age + (50 - your_age), "when you turn 50.")