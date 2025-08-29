from ExtraFunctions.LinkedListFromArray import *

def delete_duplicates(head):
    left, right = head, head
    while right:
        if right.val != left.val:
            left.next = right
            left = right

        right = right.next
    left.next = None

    return head

nums = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 8]
head = create_linked_list_from_list(nums)
result = delete_duplicates(head)
print_linked_list(result)