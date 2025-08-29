from ExtraFunctions.LinkedListFromArray import *

class Solution:
    def mergeKLists(self, lists):
        def check_empty(heads):
            for head in heads:
                if head:
                    return False
            return True

        def find_smallest(heads):
            smallest = float("inf")
            index = -1

            for i in range(len(heads)):
                if heads[i] and heads[i].val < smallest:
                    smallest = heads[i].val
                    index = i

            return smallest, index

        head = ListNode()
        current = head

        while not check_empty(lists):
            smallest, index = find_smallest(lists)
            current.next = ListNode(smallest)
            current = current.next
            lists[index] = lists[index].next

        return head.next

arrays = [[1,4,5],[1,3,4],[2,6]]
lists = []

for array in arrays:
    lists.append(create_linked_list_from_list(array))

for list in lists:
    print_linked_list(list)

solution = Solution()
merged = solution.mergeKLists(lists)

print("Merged Linked List:")
print_linked_list(merged)
