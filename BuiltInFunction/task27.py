# TODO 27 :  take two inputs and output how many times stirng 2 appears in sting 1 
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
count = 0
for i in range(len(string1) - len(string2) + 1):
    if string1[i:i+len(string2)] == string2:
        count += 1
print(count) 