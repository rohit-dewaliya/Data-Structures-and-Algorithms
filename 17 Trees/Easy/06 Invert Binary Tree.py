from ExtraFunctions.ListToTree import *

def invert_tree(root):
    if not root:
        return
    if not root.left and not root.right:
        return

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
head = invert_tree(root)
print_level_order(head)
