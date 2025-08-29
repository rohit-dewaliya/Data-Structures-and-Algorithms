from collections import deque

# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path(root, targetSum):
    if root is None:
        return False

    def backtrack(node, current_sum):
        current_sum += node.val

        if node.left is None and node.right is None:
            return current_sum == targetSum

        if node.left and backtrack(node.left, current_sum):
            return True
        if node.right and backtrack(node.right, current_sum):
            return True

        return False

    return backtrack(root, 0)


def list_to_tree(data):
    if not data or data[0] is None:
        return None

    # Create root
    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    # Build tree using BFS
    while queue and i < len(data):
        node = queue.popleft()

        # Left child
        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1

    return root

# Example usage
arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree_root = list_to_tree(arr)
print(has_path(tree_root, 22))