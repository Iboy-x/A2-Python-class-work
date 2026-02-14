# TODO 48: Maek a bubble sort function that takes an array as parameter and returns sorted array 

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