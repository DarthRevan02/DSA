def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def Goldbach(n):
    result = []
    
    for a in range(2, n // 2 + 1):
        b = n - a
        if is_prime(a) and is_prime(b):
            result.append((a, b))
    
    return result


# Input
n = int(input("Enter an even integer greater than 2: "))
print(Goldbach(n))