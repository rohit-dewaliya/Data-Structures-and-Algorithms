from ExtraFunctions.ListToTree import *

def binary_tilt_tree(root):
    tilt_sum = 0

    def tilt(node):
        nonlocal tilt_sum
        if node is None:
            return 0

        left = tilt(node.left)
        right = tilt(node.right)

        tilt_sum += abs(left - right)

        return node.val + left + right

    tilt(root)
    return tilt_sum

root = list_to_tree([4, 2, 9, 3, 5, None, 7])
result = binary_tilt_tree(root)
print(result)