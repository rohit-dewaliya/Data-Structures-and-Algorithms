def leaders(arr):
    n = len(arr)
    leaders_arr = [arr[n - 1]]

    largest = arr[n - 1]

    for i in range(n - 2, -1, -1):
        if arr[i] >= largest:
            leaders_arr.append(arr[i])
            largest = arr[i]

    return leaders_arr[ : :-1]


arr = [10, 4, 2, 4, 1]
print(leaders(arr))
