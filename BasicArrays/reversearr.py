def reverseArr(arr):
    n = len(arr)
    i = 0
    j = n-1
    while(i<j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1
        j-=1
    return arr

arr= [1,2,3,5]
print(reverseArr(arr))

