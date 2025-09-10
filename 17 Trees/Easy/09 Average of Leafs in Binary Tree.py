from ExtraFunctions.ListToTree import *

def average(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_sum = 0
        count = len(queue)

        for _ in range(count):
            node = queue.pop(0)
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(round(level_sum / count, 5))

    return result


root = list_to_tree([3, 9, 20, None, None, 15, 7])
print(average(root))