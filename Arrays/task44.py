# TODO 44: Use the array from the task 39 and find the shortest name 

arr = ['ALI', 'moiz', 'ana', 'amna', 'shiekh', 'wali', 'w']

for i in range(len(arr)):
    shortestW = arr[0]

    if len(shortestW) > len(arr[i]):
        shortestW = arr[i]
    
print(shortestW)