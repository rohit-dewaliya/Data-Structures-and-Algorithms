# Using Tabulation---------------------#
def count_construct(target, word_bank):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(0, len(table)):
        for word in word_bank:
            if target[i: i + len(word)] == word:
                table[i + len(word)] += table[i]

    return table[len(target)]


# Using Memoization-----------------#
# def count_construct(target, word_bank, memo = {}):
#     if target in memo:
#         return memo[target]
#
#     if target == '':
#         return 1
#
#     count = 0
#     for word in word_bank:
#         if target.startswith(word):
#             result = count_construct(target.removeprefix(word), word_bank)
#             count += result
#
#     memo[target] = count
#     return count


target = "abcdef"
word_bank = ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']
print(count_construct(target, word_bank))