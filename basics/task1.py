#take your age age as input and output your age afrer 5 years, 10 years, 15 years
#and your age 5 years ago and 10 year ago


# how to take inputs 
#input(prompt)
#by default are string inputs 
#to convert data type use casting 
#int() float() str()
age = int(input("Enter your age: "))
print("Your age after 5 years will be:", age + 5)
print("Your age after 10 years will be:", age + 10)
print("Your age after 15 years will be:", age + 15)
print("Your age 5 years ago was:", age - 5)
print("Your age 10 years ago was:", age - 10)