def max_area(height):
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
        max_area = max(max_area, min(height[right], height[left]) * (right - left))

        if height[right] < height[left]:
            right -= 1
        elif height[right] > height[left]:
            left += 1
        else:
            left +=1

    return max_area


height = [1,1]
result = max_area(height)
print(result)
