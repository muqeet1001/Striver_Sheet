def GCD(n1,n2):
    n1_list = []
    n2_list = []
    for i in range(1,n1+1):
        if(n1%i == 0):
            n1_list.append(i)
    for j in range(1,n2+1):
        if(n2%j == 0):
            n2_list.append(j)
    common = set(n1_list) & set(n2_list)
    return max(common)

def LCM(n1,n2):
    lcm = (n1*n2)//(GCD(n1,n2))
    return lcm

print(LCM(4,12))