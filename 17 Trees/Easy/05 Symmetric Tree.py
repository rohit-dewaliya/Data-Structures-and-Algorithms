from ExtraFunctions.ListToTree import *

def symmetric_tree(root):
    def backtrack(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return backtrack(p.left, q.right) and backtrack(p.right, q.left)
    return backtrack(root.left, root.right)

root = list_to_tree([1,2,2,None,3,None,3])
print(symmetric_tree(root))