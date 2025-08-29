import time
def convert(num):
    negative = False
    if num < 0:
        negative = True

    num = abs(num)
    temp = num
    resultant_num = 0
    digits = 0

    while temp > 0:
        digits += 1
        temp = temp // 10

    digits -= 1

    while num > 0:
        n = num % 10
        num = num // 10
        resultant_num += n * 10**digits
        digits -= 1

    if negative:
        resultant_num *= -1

    if not -2 ** 31 < resultant_num < 2 ** 31 - 1:
        return 0

    return resultant_num


x = -123
result = convert(x)
print(result)