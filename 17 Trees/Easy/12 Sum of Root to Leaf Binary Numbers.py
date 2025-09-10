from pyasn1.type import char

from ExtraFunctions.ListToTree import *

def sum_root_to_leaf(root):
    binary_sum = 0

    def str_binary(b):
        _len = len(b)
        num = 0
        for i in range(_len):
            num += int(b[_len - 1 - i]) * 2 ** i
        return num


    def backtrack(node, char):
        nonlocal binary_sum

        char += str(node.val)

        if not node.left and not node.right:
            binary_sum += str_binary(char)
            return

        if node.left:
            backtrack(node.left, char)
        if node.right:
            backtrack(node.right, char)
        return

    backtrack(root, "")
    return binary_sum


root = list_to_tree([1, 0, 1, 0, 1, 0, 1])
print(sum_root_to_leaf(root))