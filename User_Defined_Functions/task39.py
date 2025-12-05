# TODO 39: take two string parameters and return the largest common substring 
# Example : racecar, carracer ==> race 

def findlongest(str1, str2):

    Newstr = ""
    if len(str1) > len(str2):
        Gstr = str1
        Sstr = str2
    else:
        Gstr = str2
        Sstr = str1
    
    for i in range(len(Sstr)):
        for j in range(i+1, len(Sstr)+1):
            substr = Sstr[i:j]
            if substr in Gstr:
                if len(substr) > len(Newstr):
                    Newstr = substr
    return Newstr

print(findlongest("racecar", "carracer"))