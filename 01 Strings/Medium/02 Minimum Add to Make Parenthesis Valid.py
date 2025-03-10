def min_valid_parenthesis(s):
    max_count = 0
    count = 0
    for i in s:
        if count < 0:
            max_count += abs(count)
        if i == '(':
            count += 1
        else:
            count -= 1
    if max_count > 0:
        max_count += count
    return max_count


s = "())"
print(min_valid_parenthesis(s))