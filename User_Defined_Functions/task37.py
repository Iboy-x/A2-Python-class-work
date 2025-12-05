# TODO 37: Take a parameter and return TRUE if all characters are Uppercase otherwise false 

def CheckUcase ( inString):
    if inString.upper() != inString:
        return False
    else:
        return True

x = CheckUcase("HELLO")
print(str(x))