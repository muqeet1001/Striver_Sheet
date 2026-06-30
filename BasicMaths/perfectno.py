def perfect_number(n):
    sum = 0;
    for i in range(1,n):
        if(n%i == 0):
            print(i)
            sum +=i
    if(sum==n):
        return True
    return False
print(perfect_number(28))
         
            