class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    temp = head
    return head

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

temp = root
while temp:
    print(f'{temp.val} -> ', end=" ")
    temp = temp.next
print('None')