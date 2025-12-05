# TODO 34: Create a function that takes a sentence as a string parameter and returns the length of last word

def x(string1):
    i = len(string1) -1 
    length = 0 
    while string1[i] != " ":
        i -= 1
        length += 1
    return(length)

print( x("Hello world"))