def fruit_baskets(fruits):
    n = len(fruits)
    index_hash = {}
    left = 0
    count = float('-inf')

    for right in range(n):
        fruit = fruits[right]

        if fruit not in index_hash and len(index_hash) == 2:
            min_fruit = min(index_hash, key=lambda k: index_hash[k])
            left = index_hash[min_fruit] + 1
            index_hash.pop(min_fruit)

        index_hash[fruit] = right

        count = max(count, right - left + 1)

    return count

# Test
fruits = [1, 2,1, 3, 1]
result = fruit_baskets(fruits)
print(result)  # Output: 4
