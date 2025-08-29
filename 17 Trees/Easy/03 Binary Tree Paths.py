from ExtraFunctions.ListToTree import list_to_tree

def binary_tree_paths(root):
    result = []
    if root is None:
        return result

    def backtrack(node, path):
        if not node.left and not node.right:
            path += str(node.val)
            result.append(path[:])
            return
        else:
            path += str(node.val) + "->"

        if node.left:
            backtrack(node.left, path)
        if node.right:
            backtrack(node.right, path)

    backtrack(root, "")
    return result

arr = [1]
tree_root = list_to_tree(arr)
print(binary_tree_paths(tree_root))