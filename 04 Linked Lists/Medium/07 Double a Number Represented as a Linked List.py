from ExtraFunctions.LinkedListFromArray import *

def double_number(head):
    temp = head
    carry = 0

    def backtrack(node):
        nonlocal carry
        if not node:
            return

        backtrack(node.next)
        val = node.val * 2 + carry
        carry = val // 10
        val = val % 10

        node.val = val

    backtrack(head)

    if carry:
        node = ListNode(carry)
        node.next = head
        head = node
    return head

head = create_linked_list_from_list([9, 8, 9])
print_linked_list(double_number(head))