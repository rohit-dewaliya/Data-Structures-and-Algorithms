from ExtraFunctions.ListToTree import *

def sum_of_left_leaves(root):
    _sum = 0

    def recurse(root):
        nonlocal _sum
        if not root:
            return

        if root.left:
            if not root.left.left and not root.left.right:
                _sum += root.left.val
            recurse(root.left)
        if root.right:
            recurse(root.right)
        return
    recurse(root)
    return _sum

root = list_to_tree([3, None, 5, 7])
result = sum_of_left_leaves(root)
print(result)