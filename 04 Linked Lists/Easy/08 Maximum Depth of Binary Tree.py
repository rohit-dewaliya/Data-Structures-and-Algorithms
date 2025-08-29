from ExtraFunctions.ListToTree import *

def maximum_depth(root):
    depth = 0

    if root is None:
        return 0

    def traverse(node, count):
        if not node.left and not node.right:
            nonlocal depth
            depth = max(depth, count + 1)
            return

        count += 1
        if node.left:
            traverse(node.left, count)
        if node.right:
            traverse(node.right, count)

    traverse(root, 0)
    return depth

root = list_to_tree([3, None, 7])
print(maximum_depth(root))