# take three string and  output them as one string as camel case 

def CamleCase(str1, str2, str3):
    str1 = str1.lower()
    str2 = str2[0].upper() + str2[1::] 
    str3 = str3[0].upper() + str3[1::]


    return str1+str2+str3
print(CamleCase("Hello", "world", "lol"))