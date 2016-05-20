def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        currentVal = arr[i]
        currentPos = i
        
        while currentPos > 0 and arr[currentPos-1] > currentVal:
            arr[currentPos] = arr[currentPos-1]
            currentPos = currentPos - 1
        arr[currentPos] =  currentVal
    return arr

data_array = [2,4,6,8,1,3,5,7]
sorted_array = insertion_sort(data_array)
print sorted_array
