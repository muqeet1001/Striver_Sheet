arr = [1,2,3,4,5]
arr2=[5,4,6,7,8]
n = len(arr)

def checksorted(arr,n):
    j = 0
    for i in range(1,n):
         if(arr[j]>arr[i]):
            return False
         j+=1
    return True
    
print(checksorted(arr2,n))