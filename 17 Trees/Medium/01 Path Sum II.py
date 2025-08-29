from ExtraFunctions.ListToTree import list_to_tree

# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path(root, targetSum):
    results = []

    if root is None:
        return results

    def backtrack(node, current_sum, nums):
        nums.append(node.val)
        current_sum += node.val

        if not node.left and not node.right:
            if current_sum == targetSum:
                results.append(nums[:])
        else:
            if node.left:
                backtrack(node.left, current_sum, nums)
            if node.right:
                backtrack(node.right, current_sum, nums)

        nums.pop()

    backtrack(root, 0, [])
    return results


# Example usage
arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
tree_root = list_to_tree(arr)
print(has_path(tree_root, 22))