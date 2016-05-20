def bubble_sort(arr):
    
    '''
    Bubble Sort : 
        From the given data list, compares current item with the next item
        and exchanges their positions
    '''
    exchanges = True
    index_pos = len(arr)-1
    
    while index_pos > 0 and exchanges:
        exchanges = False
        for i in range(index_pos):
            if arr[i] > arr[i+1]:
                exchanges = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        index_pos -= 1
    return arr

data_array = [2,5,7,3,4,6]
sorted_data_array = bubble_sort(data_array)
print sorted_data_array
