mystring = "cedar college"
print(len(mystring))#len(string)=>number of characters
print(mystring[0])# string[postion]=> character position
print(mystring[3])
print(mystring[0:3]) #[start:end](exclusive of end)
print(mystring[0:10]) # defult start =0
print(mystring[3:])# defult end= length of the string
print(mystring[-3])#length -3
print(mystring[3:-3])
print(mystring[::2])# [start:end:iteration]
print(mystring[::-1])# print backwards
print(mystring.upper())
print(mystring.lower())
print(ord("A")) # ACII value
print(chr(97))# ACII character
mystring = "   cedar   "
print(mystring.strip())
newstring=mystring.strip()+"hello\n"+mystring.strip()# + => concat
print(newstring)