def reverse_string(s):
    result = []

    def recurse(s, i):
        if i == len(s) - 1:
            return s[i]

        result.append(recurse(s, i + 1))

        return s[i]

    def swaps(left, right):
        if left >= right:
            return

        s[left], s[right] = s[right], s[left]
        swaps(left + 1, right - 1)

    swaps(0, len(s) - 1)


    # recurse(s, -1)
    return s

s = ["h","e","l","l","o"]
print(reverse_string(s))