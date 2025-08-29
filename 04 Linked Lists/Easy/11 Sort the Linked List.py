from ExtraFunctions.LinkedListFromArray import *

def sort_linked_list(head):
    def merge(left, right):
        dummy = ListNode(None)
        temp = dummy

        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next

        if left:
            temp.next = left
        if right:
            temp.next = right

        return dummy.next

    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sort_linked_list(head)
    right = sort_linked_list(mid)

    return merge(left, right)


head = create_linked_list_from_list([4, 2, 1, 6, 4, 9, 7, 8])
print_linked_list(sort_linked_list(head))
