def fruits_baskets(fruits, baskets):
    n = len(fruits)
    unplaced_fruits = 0
    placed_fruits = [False] * n

    for i in range(n):
        placed = False  
        for j in range(n):
            if not placed_fruits[j] and fruits[i] <= baskets[j]:
                placed_fruits[j] = True
                placed = True
                break
        if not placed:
            unplaced_fruits += 1

    return unplaced_fruits

fruits = [8, 5]
baskets = [1, 8]
result = fruits_baskets(fruits, baskets)
print(result)