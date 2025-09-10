from ExtraFunctions.LinkedListFromArray import *

def modify_list(nums, head):
    nums = set(nums)
    temp = head
    prev = None

    while temp:
        if temp.val in nums:
            if temp.next:
                temp.val = temp.next.val
                temp.next = temp.next.next
            else:
                prev.next = None
                temp = None
        else:
            prev = temp
            temp = temp.next

    return head

head = create_linked_list_from_list([1, 2, 1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 1, 3])
nums = [1, 2, 3]
print_linked_list(modify_list(nums, head))