def min_remove(s):
    n = len(s)
    s = list(s)
    stack = []

    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''

    while stack:
        s[stack.pop()] = ''

    return ''.join(s)


testcases = [
    "lee(t(c)o)de)",
    "a)b(c)d",
    "))((",
    "(a(b(c)d)"
]

for testcase in testcases:
    print(min_remove(testcase))
