def xor_queries(arr, queries):
    n = len(arr)
    result = [arr[0]]
    _xor = arr[0]
    for i in range(1, n):
        _xor ^= arr[i]
        result.append(_xor)

    _xor_arr = []
    for i in range(0, len(queries)):
        if queries[i][0] == 0:
            _xor_arr.append(result[queries[i][1]])
        else:
            _xor_arr.append(result[queries[i][1]] ^ result[(queries[i][0] - 1)])
    return _xor_arr

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]
print(xor_queries(arr, queries))