from collections import deque

# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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