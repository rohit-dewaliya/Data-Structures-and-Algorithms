# Using Tabulation---------------------#
def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for word in word_bank:
            if i + len(word) <= len(target) and target[i: i + len(word)] == word:
                new_combination = [[word] + way for way in table[i]]
                table[i + len(word)].extend(new_combination)

    return table[len(target)]


# Using Memoization-----------------#
# def all_construct(target, word_bank, memo = {}):
#     if target in memo:
#         return memo[target]
#
#     if target == '':
#         return [[]]
#
#     result = []
#
#     for word in word_bank:
#         if target.startswith(word):
#             suffix = target[len(word):]
#             suffix_ways = all_construct(suffix, word_bank)
#             target_ways = [[word] + way for way in suffix_ways]
#             result.extend(target_ways)
#
#     memo[target] = result
#     return result


target = "abcdef"
word_bank = ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']
print(all_construct(target, word_bank))
