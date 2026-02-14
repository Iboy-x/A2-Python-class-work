# TODO 47: Make a function takes an integer array and a target integer value as paramter return indices of the two numbers such that they add upto target otherwise return -1 aws both indices
#Example : [1,3,7,11] target = 8
# return [0,2]

arr = [9, 7, 8, 2]
target = 8 

def findTarget(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)-1, 0, -1):
            if (arr[i] + arr[j] == target):
                return[i, j]
    return -1
            

print(findTarget(arr, target))










'''def findTarget(arr, target):
    n = 0
    for i in range(len(arr)): # 0 - 3
        for j in range(len(arr)-1, n, -1): #1
            if arr[i] + arr[j] == target :
                res = [i, j]
                return res
            else:
                res = -1 
    n += 1
    return res
        
    

print(findTarget(arr, target))'''