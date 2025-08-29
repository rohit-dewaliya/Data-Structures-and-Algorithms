from ExtraFunctions.LinkedListFromArray import *

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        temp = head

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        temp.next = list1 if list1 else list2
        return head.next


list1 = create_linked_list_from_list([1, 2, 4])
list2 = create_linked_list_from_list([1, 3, 4])

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

print("Merged Linked List:")
print_linked_list(merged)
