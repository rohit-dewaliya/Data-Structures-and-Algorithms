def reverse_bits(n):
    bits = format(n, '032b')
    bits = bits[::-1]

    num = 0
    for i in range(0, 32):
        num += int(bits[31 - i]) * 2 ** i

    return num

n = 4
print(reverse_bits(n))