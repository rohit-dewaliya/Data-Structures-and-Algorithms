from ExtraFunctions.LinkedListFromArray import *

def reverse(head):
    # Method I-------------#
    # prev = None
    # current = head
    #
    # while current:
    #     new_node = current.next
    #     current.next = prev
    #     prev = current
    #     current = new_node
    #
    # return prev

    # Method II------------#
    if not head or not head.next:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head


head = create_linked_list_from_list([1, 2, 3, 4, 5])
result = reverse(head)
print_linked_list(result)