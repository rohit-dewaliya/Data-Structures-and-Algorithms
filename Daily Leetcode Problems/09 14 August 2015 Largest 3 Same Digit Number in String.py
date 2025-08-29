def largest_good_number(num):
    # METHOD I-----------------------#
    # n = len(num)
    # max_num = ""
    # temp_num = num[0]
    # count = 1
    #
    # for i in range(1, n):
    #     if num[i] == temp_num:
    #         count += 1
    #     else:
    #         temp_num = num[i]
    #         count = 1
    #
    #     if count == 3:
    #         triple = temp_num * 3
    #         if max_num == "" or triple > max_num:
    #             max_num = triple
    #
    # return max_num

    # METHOD II-------------------#
    nums = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
    for n in nums:
        if n in num:
            return n
    return ""


num = "677713333999"
print(largest_good_number(num))