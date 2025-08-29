from collections import deque

# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root):
    if root is None:
        return 0

    def backtrack(node, _sum):
        _sum = _sum * 10 + node.val
        if node.left is None and node.right is None:
            return _sum

        sum_1, sum_2 = 0, 0
        if node.left:
            sum_1 = backtrack(node.left, _sum)
        if node.right:
            sum_2 = backtrack(node.right, _sum)

        return sum_1 + sum_2

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
arr = [1, 2, 3]
tree_root = list_to_tree(arr)
print(sum_numbers(tree_root))