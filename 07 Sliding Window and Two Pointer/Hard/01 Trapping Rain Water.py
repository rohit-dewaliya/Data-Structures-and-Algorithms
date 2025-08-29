def trap(height):
    n = len(height)
    left = height[:]
    right = height[:]

    for i in range(1, n):
        left[i] = max(left[i-1], height[i])

    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], height[i])

    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - height[i]
    return water

height = [4, 2, 0, 3, 2, 5]
result = trap(height)
print(result)