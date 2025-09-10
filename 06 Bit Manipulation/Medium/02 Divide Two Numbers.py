def divide_num(dividend, divisor):
    if dividend == 0:
        return 0

    negative = (dividend < 0) ^ (divisor < 0)

    int_max = 2 ** 31 - 1
    int_min = -2 ** 31

    if dividend == int_min and divisor == -1:
        return int_max

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    for shift in range(31, -1, -1):
        if (divisor << shift) <= dividend:
            dividend -= (divisor << shift)
            quotient += (1 << shift)

    if negative:
        quotient = -quotient

    return quotient


dividend = 10
divisor = 3
print(divide_num(dividend, divisor))