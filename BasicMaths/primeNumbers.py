def prime(n):
    count = 0;
    for i in range(1,n+1):
        if(n%i == 0):
            count+=1
        if(count>2):
            return False
    return True


def prime_gpt(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return count == 2


def count_prime(n):
    count = 0
    for i in range(n+1):
        if(prime_gpt(i)):
            count+=1
    return count

print(count_prime(20))