from ExtraFunctions.LinkedListFromArray import *

class Solution:
    def removeNthFromEnd(self, head, n):
        # METHOD I --------------------------------#
        # temp = head
        #
        # l = 0
        #
        # while temp:
        #     temp = temp.next
        #     l += 1
        #
        # if l == n:
        #     return head.next
        #
        # n = l - n - 1
        #
        # temp = head
        # for _ in range(n):
        #     temp = temp.next
        #
        # if temp.next:
        #     temp.next = temp.next.next
        #
        # return head


        # METHOD II --------------------------------#
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


head = create_linked_list_from_list([1, 2, 3, 4, 5])
n = 3

solution = Solution()
merged = solution.removeNthFromEnd(head, n)

print("Merged Linked List:")
print_linked_list(merged)
