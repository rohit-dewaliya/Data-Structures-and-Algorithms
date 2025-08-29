def generate_parentheses(n):
    result = []

    def backtrack(para, open_counts, close_counts):
        if open_counts == n and close_counts == n:
            result.append(para)
            return

        if open_counts < n:
            backtrack(para + "(", open_counts + 1, close_counts)

        if close_counts < open_counts:
            backtrack(para + ")", open_counts, close_counts + 1)

    backtrack("", 0, 0)
    return result

n = 3
print(generate_parentheses(n))
