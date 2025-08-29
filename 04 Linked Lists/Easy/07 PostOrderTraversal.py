from ExtraFunctions.ListToTree import *

def postorder_traversal(root):
    result = []
    if root is None:
        return []

    def traverse(node):
        if not node:
            return []
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)
        return result

    traverse(root)
    return result

root = list_to_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
print(postorder_traversal(root))