# TODO 36:  make a function that takes a string parameter and return a string with revered vowels without using the list approach
# Example : icecream => i e e a ==> acecreim

def reverseVowels(s):
    vowels = "aeiouAEIOU"
    newVowel = ""
    for i in s: 
        if i in vowels:
            newVowel = i + newVowel 
    revStr = ""
    pos = 0
    for i in s:
        if i not in vowels:
            revStr += i
        else: 
            revStr += newVowel[pos]
            pos += 1
    return revStr
        

print(reverseVowels("icecream"))

