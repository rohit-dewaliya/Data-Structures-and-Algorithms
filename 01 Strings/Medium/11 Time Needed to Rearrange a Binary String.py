def time_needed(s):
    # Method I--------------------------------#
    # def get_indexes(s):
    #     indexes = []
    #     for i in range(len(s) - 1):
    #         if s[i] == "0" and s[i + 1] == "1":
    #             indexes.append(i)
    #
    #     return indexes
    #
    # s = list(s)
    # time = 0
    #
    # while True:
    #     indexes = get_indexes(s)
    #     if not indexes:
    #         break
    #
    #     for index in indexes:
    #         s[index], s[index + 1] = s[index + 1], s[index]
    #
    #     time += 1
    #
    # return time

    # Method II---------------------------------#
    zero_count = 0
    time = 0

    for ch in s:
        if ch == '0':
            zero_count += 1
        elif zero_count > 0:
            time = max(time + 1, zero_count)

    return time


s = "0110101"
result = time_needed(s)
print(result)