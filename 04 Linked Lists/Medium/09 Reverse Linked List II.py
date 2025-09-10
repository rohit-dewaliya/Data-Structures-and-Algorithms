from ExtraFunctions.LinkedListFromArray import *

def reverse_linked_list(head, left, right):
    if not head or not head.next:
        return head

    prev = None
    temp = head

    for _ in range(1, left):
        prev = temp
        temp = temp.next

    head_1 = temp

    for _ in range(left, right):
        temp = temp.next

    next_sublist = temp.next
    temp.next = None

    def reverse(node):
        if not node or not node.next:
            return node
        head_r = reverse(node.next)
        node.next.next = node
        node.next = None
        return head_r

    new_head = reverse(head_1)

    if prev:
        prev.next = new_head
    else:
        head = new_head

    tail = new_head
    while tail.next:
        tail = tail.next

    tail.next = next_sublist

    return head


head = create_linked_list_from_list([1, 2, 3, 4, 5])
left = 2
right = 4
root = reverse_linked_list(head, left, right)
print_linked_list(root)