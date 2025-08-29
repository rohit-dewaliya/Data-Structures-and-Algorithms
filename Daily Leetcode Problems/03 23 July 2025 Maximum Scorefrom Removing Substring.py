def maximum_score(s, x, y):
    n = len(s)

    def remove_pairs(s, first, second, score):
        stack = []
        _score = 0

        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                _score += score
            else:
                stack.append(ch)

        return "".join(stack), _score

    if x > y:
        s, score_1 = remove_pairs(s, 'a', 'b', x)
        _, score_2 = remove_pairs(s, 'b', 'a', y)
    else:
        s, score_1 = remove_pairs(s, 'b', 'a', y)
        _, score_2 = remove_pairs(s, 'a', 'b', x)

    return score_1 + score_2


testcases = [
    [
        "aabbaaxybbaabb",
        5,
        4
    ],

    [
        "cdbcbbaaabab",
        4,
        5
    ],

    [
        "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha",
        1926,
        4320
    ],

    [
        "ababababababababababababababababababababababababababababababababababababababababababababababababab",
        3,
        2
    ],

    [
        "babababababababababababababababababababababababababababababababababababababababababababababababababababa",
        6,
        7
    ],

    [
        "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba",
        8,
        9
    ],

    [
        "aaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbbaaaaaaaaabbbbbbbbbb",
        10,
        1
    ],

    [
        "aabbabbaabbabbaabbabbaabbabbaabbabbaabbabbaabbabbaabbabbaabbabbaabbabbaabbabbaabbabbaabbabbaabbab",
        9,
        11
    ],

    [
        "bbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",
        8,
        9
    ]
]
num = 1
for testcase in testcases:
    result = maximum_score(testcase[0], testcase[1], testcase[2])
    print(f"Testcase {num}\t", result)
    num += 1

