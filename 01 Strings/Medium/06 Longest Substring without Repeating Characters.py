def longest_substring(s):
    length = 0
    l = len(s)
    left = 0
    freq = {}

    for right in range(0, l):
        while s[right] in freq:
            freq.pop(s[left])
            left += 1
        freq[s[right]] = 1
        length = max(length, right - left + 1)

    return length

s = "abcabcbb"
print(longest_substring(s))