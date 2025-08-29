def min_valid_parenthesis(s):
    # Method I----------------------------------#
    # stack = []
    #
    # for b in s:
    #     if not stack:
    #         stack.append(b)
    #     elif b == ")" and stack[-1] == "(":
    #         stack.pop()
    #     else:
    #         stack.append(b)
    #
    # return len(stack)
    
    # Method II----------------------------------#
    open_count = 0
    close_count = 0

    for b in s:
        if b == '(':
            open_count += 1
        elif b == ')' and open_count > 0:
            open_count -= 1
        else:
            close_count += 1

    return open_count + close_count

s = "()))(("
print(min_valid_parenthesis(s))
