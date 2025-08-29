def add_binary(a, b):
    result = ""
    m, n = len(a) - 1, len(b) - 1
    sum_table = {3: ["1", 1], 2: ["0", 1], 1: ["1", 0], 0: ["0", 0]}
    carry = 0

    while m >= 0 or n >= 0:
        if m < 0:
            num_1 = 0
        else:
            num_1 = ord(a[m]) - ord("0")

        if n < 0:
            num_2 = 0
        else:
            num_2 = ord(b[n]) - ord("0")

        _sum = num_1 + num_2 + carry
        r = sum_table[_sum]
        result += r[0]
        carry = r[1]

        m, n = m - 1, n - 1

    if carry:
        result += "1"
    return result[::-1]

a = "11"
b = "1"
result = add_binary(a, b)
print(result)