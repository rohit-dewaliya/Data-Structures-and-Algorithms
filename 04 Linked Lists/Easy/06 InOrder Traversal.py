from ExtraFunctions.ListToTree import *

def inorder_traversal(root):
    result = []
    if root is None:
        return []

    def traverse(node):
        if not node:
            return []
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
        return result

    traverse(root)
    return result

root = list_to_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
print(inorder_traversal(root))