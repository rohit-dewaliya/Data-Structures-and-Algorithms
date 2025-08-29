from ExtraFunctions.LinkedListFromArray import *

def palindrome(head):

    def backtrack(node):
        if not node.next:
            return head.val == node.val

        if backtrack(node.next):
            return head.val == node.val
        return False

    return backtrack(head)

head = create_linked_list_from_list([1, 2, 3, 4, 5, 6])
print(palindrome(head))