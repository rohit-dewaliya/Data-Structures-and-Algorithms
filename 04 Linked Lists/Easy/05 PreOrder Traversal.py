from ExtraFunctions.ListToTree import *

def preorder_traversal(root):
    result = []

    def traverse(node):
        if not node:
            return []
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
        return result

    traverse(root)
    return result

root = list_to_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
print(preorder_traversal(root))