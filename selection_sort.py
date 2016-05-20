def selection_sort(arr):
    '''
    selection sort :
        Requires (n-1) passes to sort n items
        For each pass max/min in proper position ans starts checking for the remaining items
    '''

    for slot in range(len(arr)-1, 0, -1):
        maxIndex = 0
        
        for location in range(1, slot+1):
            if arr[location] > arr[maxIndex]:
                maxIndex = location
                
        temp = arr[slot]
        arr[slot] = arr[maxIndex]
        arr[maxIndex] = temp
    return arr

data_array = [2,4,3,6,7,9,8]
sorted_array = selection_sort(data_array)
print sorted_array
