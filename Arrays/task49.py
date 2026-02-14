# TODO 49: Make a function that takes an array as parameter and sorts the array using the function from TASK 44 and removes any duplicates in the array return final array 

arr = [8, 9, 4, 5, 6, 7, 2, 1, 3]

def bubbleSort(arr):
    n = len(arr) - 1
    for i in range( len(arr)-1):
        for j in range( n):
            if (arr[i] > arr[i+1 ]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j]= temp
        n -= 1
    return arr



print(bubbleSort(arr))