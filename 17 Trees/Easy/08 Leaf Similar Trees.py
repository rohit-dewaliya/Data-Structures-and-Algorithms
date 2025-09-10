from ExtraFunctions.ListToTree import *

def leaf_similarity(root1, root2):
    nums1 = []
    nums2 = []

    def leaf_nodes(root, nums):
        if not root.left and not root.right:
            nums.append(root.val)
            return nums

        if root.left:
            leaf_nodes(root.left, nums)
        if root.right:
            leaf_nodes(root.right, nums)
        return nums

    nums1 = leaf_nodes(root1, nums1)
    nums2 = leaf_nodes(root2, nums2)
    return nums1 == nums2

root1 = list_to_tree([1])
root2 = list_to_tree([2])
print(leaf_similarity(root1, root2))