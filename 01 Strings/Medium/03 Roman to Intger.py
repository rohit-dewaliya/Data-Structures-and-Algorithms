def roman_to_integer(s):
    n = len(s)
    num = 0
    roman_values = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    num_values = [1, 5, 10, 50, 100, 500, 1000]
    i = n - 1
    while i >= 0:
        value = roman_values.index(s[i])
        if i > 1:
            pre = roman_values.index(s[i - 1])
            if value > pre:
                num += num_values[value] - num_values[pre]
                i -= 2
                continue
        num += num_values[value]
        i -= 1

    return num

s = 'MCMXCIV'
print(roman_to_integer(s))