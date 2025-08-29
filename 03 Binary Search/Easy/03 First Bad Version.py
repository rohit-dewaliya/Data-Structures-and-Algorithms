# The isBadVersion API is already defined for you.
def isBadVersion(version):
    pass

def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

n = 5
print(firstBadVersion(n))
