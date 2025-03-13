# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m, n, head):
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        index = 0
        temp = head

        while left < right and top < bottom:
            # Moving to Right
            for i in range(left, right):
                if temp is None:
                    break
                matrix[top][i] = temp.val
                temp = temp.next
            top += 1

            # Moving Down
            for i in range(top, bottom):
                if temp is None:
                    break
                matrix[i][right - 1] = temp.val
                temp = temp.next
            right -= 1

            if not (left < right and top < bottom):
                break

            # Moving to Left
            for i in range(right - 1, left - 1, -1):
                if temp is None:
                    break
                matrix[bottom - 1][i] = temp.val
                temp = temp.next
            bottom -= 1

            # Moving Up
            for i in range(bottom - 1, top - 1, -1):
                if temp is None:
                    break
                matrix[i][left] = temp.val
                temp = temp.next
            left += 1

        return matrix