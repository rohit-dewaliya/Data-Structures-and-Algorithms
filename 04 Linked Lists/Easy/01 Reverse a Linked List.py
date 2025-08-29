from ExtraFunctions.LinkedListFromArray import *
def reverse_list(head):
    if head == None or head.next == None:
        return head

    temp = head
    prev = head
    curr = head.next
    next = curr.next

    if next == None:
        head = curr
        curr.next = prev
        prev.next = None
        return head

    temp = head
    return head

root = create_linked_list_from_list([1, 2, 3, 4, 5, 6, 7])
head = reverse_list(root)
print_linked_list(head)