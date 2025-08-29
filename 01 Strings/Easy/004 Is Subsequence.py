def isSubsequence(s, t):
    m, n = len(s), len(t)
    first, second = 0, 0

    while first < m and second < n:
        if s[first] == t[second]:
            first += 1
        second += 1

    return first == m

s = "axc"
t = "ahbgdc"
result = isSubsequence(s, t)
print(result)