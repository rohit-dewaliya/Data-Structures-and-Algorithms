from ExtraFunctions.LinkedListFromArray import *

def odd_even_linked_list(head):
    # Method I-----------------------#
    # odd_dummy = ListNode(0)
    # even_dummy = ListNode(0)
    #
    # odd, even = odd_dummy, even_dummy
    # is_odd = True
    #
    # while head:
    #     print()
    #     if is_odd:
    #         odd.next = head
    #         odd = odd.next
    #     else:
    #         even.next = head
    #         even = even.next
    #     head = head.next
    #     is_odd = not is_odd
    #
    # even.next = None
    # odd.next = even_dummy.next
    #
    # return odd_dummy.next

    # Method II-----------------------#
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head

head = create_linked_list_from_list([2, 1, 3, 5, 6, 4, 7])
print_linked_list(odd_even_linked_list(head))