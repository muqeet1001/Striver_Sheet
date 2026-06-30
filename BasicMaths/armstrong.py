def arms(N):
    original_n = N
    sum = 0
    while(N>0):
        digi = N%10
        sum += digi ** 3
        print(sum)
        N = N//10
    if original_n == sum:
        return True
    return False
    
print(arms(370))