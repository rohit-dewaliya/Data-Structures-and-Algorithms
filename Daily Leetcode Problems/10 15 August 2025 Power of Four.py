def power_of_four(n):
    if n < 1:
        return False

    while n > 1:
        if n % 4 == 0:
            n //= 4
        else:
            return False
    return True

n = 40
print(power_of_four(n))