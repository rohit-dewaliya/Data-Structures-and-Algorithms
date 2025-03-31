class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_loop(head):
    fast = head
    slow = head

    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    else:
        return -1

    slow = head
    count = 0
    while fast != slow:
        fast = fast.next
        slow = slow.next
        count += 1
    return count

root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
root.next.next.next.next = root.next

print(has_loop(root))