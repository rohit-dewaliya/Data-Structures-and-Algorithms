def myatoi(s):
    s = s.strip()
    if not s:
        return 0

    sign = 1
    i = 0
    n = len(s)

    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1

    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    num *= sign

    int_min, int_max = -2 ** 31, 2 ** 31 - 1
    if num < int_min:
        return int_min
    if num > int_max:
        return int_max

    return num


s = "       -1337c0d3"
print(myatoi(s))