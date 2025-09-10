from ExtraFunctions.ListToTree import *

def find_mode(root):
    if root is None:
        return []

    freq_hash = {}

    def mode(node):
        nonlocal freq_hash
        if node is None:
            return

        freq_hash[node.val] = freq_hash.get(node.val, 0) + 1
        mode(node.left)
        mode(node.right)
        return

    mode(root)
    nums = [[key, value] for key, value in freq_hash.items()]
    nums = sorted(nums, key=lambda x: x[1], reverse=True)
    result = []
    _max = nums[0][1]
    for num in nums:
        if num[1] == _max:
            result.append(num[0])
        else:
            break
    return result

root = list_to_tree([1,None,2,2])
print(find_mode(root))