from ExtraFunctions.ListToTree import *

def print_tree(root):
    if not root:
        return []

    height = 0

    def get_height(root, count):
        nonlocal height
        if not root.left and not root.right:
            count += 1
            height = max(height, count)
            return

        if root.left:
            get_height(root.left, count + 1)
        if root.right:
            get_height(root.right, count + 1)
        return

    get_height(root, 0)
    columns = 2 ** (height - 1)
    tree = [[""] * columns] * height
    return tree

root = list_to_tree([1, 2, 3, None, 4])
print(print_tree(root))
