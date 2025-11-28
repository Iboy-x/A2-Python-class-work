# TODO 29: Take an input from the user and output it as RLE 
# Hello whyyyy
# He2l0 wh4Y

x = input("Enter the string: ")
StCnt = 1 
for i in range( len(x) - 1):

    if x[i] == x[i+1]:
        StCnt += 1
    else:
        newstr = x[i]+ str(StCnt)
        print(newstr)
        StCnt = 1
        
    if i == len(x) - 2:
        newstr = x[i]+ str(StCnt)
        print(newstr )

    