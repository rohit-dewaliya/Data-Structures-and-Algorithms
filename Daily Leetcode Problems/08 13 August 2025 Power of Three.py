def isPowerOfThree(n):
    if n  <= 0:
        return False

    while n > 1:
        if n % 3 == 0:
            n = n // 3
        else:
            return False
        
    return True

n = 3
print(isPowerOfThree(n))
