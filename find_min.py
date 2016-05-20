def findMin(arr):
    minVal = arr[0]
    for i in arr[1:]:
        if i < minVal:
            minVal = i
    return minVal

a = [1,3,4,5,0,-6,8]
b = findMin(a)
print b
