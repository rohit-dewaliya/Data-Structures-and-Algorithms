class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        temp = result
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            add = l1_val + l2_val + carry
            carry = add // 10
            temp.next = ListNode(add % 10)
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result.next

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
head_1 = ListNode(l1[0])

temp = head_1
for i in range(1, len(l1)):
    temp.next = ListNode(l1[i])
    temp = temp.next

head_2 = ListNode(l2[0])
temp = head_2
for i in range(1, len(l2)):
    temp.next = ListNode(l2[i])
    temp = temp.next

head_3 = Solution().addTwoNumbers(head_1, head_2)

while head_3 is not None:
    print(head_3.val, end = ' -> ' if head_3.next else ' ')
    head_3 = head_3.next
