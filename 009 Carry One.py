def carry_one(digits):
    n = len(digits)
    carry = 0
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            digits[i] += 1
        _sum = (digits[i] + carry)
        digits[i] = _sum % 10
        carry = _sum // 10

    if carry:
        digits.insert(0, carry)

    return digits

digits = [9, 9, 9]
print(carry_one(digits))