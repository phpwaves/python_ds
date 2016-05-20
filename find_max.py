def findMax(arr):
    maxVal = arr[0]
    for i in arr[1:]:
        if i > maxVal:
            maxVal = i
    return maxVal

a = [1,3,4,5,0,-6,8]
b = findMax(a)
print b
