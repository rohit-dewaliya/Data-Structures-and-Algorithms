from ExtraFunctions.ListToTree import list_to_tree

# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path(root, targetSum):
    memo = {0: 1}

    def backtrack(node, current_sum):
        if not node:
            return 0

        current_sum += node.val
        count = memo.get(current_sum - targetSum, 0)

        memo[current_sum] = memo.get(current_sum, 0) + 1
        count += backtrack(node.left, current_sum)
        count += backtrack(node.right, current_sum)
        memo[current_sum] -= 1

        return count

    return backtrack(root, 0)


# Example usage
arr = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
tree_root = list_to_tree(arr)
print(has_path(tree_root, 8))