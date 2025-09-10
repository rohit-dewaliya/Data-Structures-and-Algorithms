def average_pass_ratio(classes, extraStudents):
    for _class in classes:
        _class.append(round(_class[0] / _class[1], 5))

    classes = sorted(classes, key = lambda x : x[2])

    return classes

classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4
print(average_pass_ratio(classes, extraStudents))