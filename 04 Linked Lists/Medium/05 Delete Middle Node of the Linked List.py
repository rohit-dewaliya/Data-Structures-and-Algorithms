from ExtraFunctions.LinkedListFromArray import *

def delete_middle_node(head):
    if not head:
        return head

    if not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head

head = create_linked_list_from_list([1])
print_linked_list(delete_middle_node(head))