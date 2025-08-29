class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list_from_list(array=[]):
    if array is None or len(array) == 0:
        return None

    head = ListNode(array[0])
    temp = head

    for i in range(1, len(array)):
        temp.next = ListNode(array[i])
        temp = temp.next

    return head

def print_linked_list(head):
    if head is None:
        print("Empty list")
        return

    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()