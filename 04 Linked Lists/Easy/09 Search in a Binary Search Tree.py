from ExtraFunctions.ListToTree import *

def search(root, val):
    # METHOD I-----------------#
    # while root:
    #     if root.val == val:
    #         return root
    #     elif val < root.val:
    #         root = root.left
    #     else:
    #         root = root.right
    # return None

    # METHOD II----------------------#
    if not root:
        return None

    if root.val == val:
        return root
    elif val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)

root = list_to_tree([4,2,7,1,3])
val = 2
print(search(root, val))