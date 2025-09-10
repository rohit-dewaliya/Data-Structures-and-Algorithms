def hamming_weight(x, y):
    count = 0
    while x > 0 or y > 0:
        bit_1 = 1 if x & 1 else 0
        bit_2 = 1 if y & 1 else 0

        if bit_1 ^ bit_2 == 1:
            count += 1

        x >>= 1
        y >>= 1
    return count

x = 5
y = 40
print(hamming_weight(x, y))
