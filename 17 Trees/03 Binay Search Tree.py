'''
# Binary Search Tree------------------------#
It's a binary such that left subtree value of a node is less than or equal to its parent node's value and in the
right subtree the value of a node is greater than its parent node's value.
'''

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root

    def insert_node(self, root_node, node_value): # Time Complexity is O(lonN) and Space Complexity O(lonN)
        if root_node.data == None:
            self.root.data = node_value
        elif node_value <= root_node.data:
            if root_node.left is None:
                root_node.left = TreeNode(node_value)
            else:
                self.insert_node(root_node.left, node_value)
        else:
            if root_node.right is None:
                root_node.right = TreeNode(node_value)
            else:
                self.insert_node(root_node.right, node_value)
        return "Node added successfully."

    def pre_order_traversal(self, root_node):
        if root_node is None:
            return
        print(root_node.data, end = " ")
        self.pre_order_traversal(root_node.left)
        self.pre_order_traversal(root_node.right)

    def in_order_traversal(self, root_node):
        if root_node is None:
            return
        self.pre_order_traversal(root_node.left)
        print(root_node.data, end=" ")
        self.pre_order_traversal(root_node.right)

    def post_order_traversal(self, root_node):
        if root_node is None:
            return
        self.pre_order_traversal(root_node.left)
        self.pre_order_traversal(root_node.right)
        print(root_node.data, end=" ")

    def level_order_traversal(self, root_node):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data, end = " ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self, root_node, value): # Time Complexity is O(lonN) and Space Complexity O(lonN)
        if root_node is None:
            return "Value not found"

        if root_node.data == value:
            return "Value is found"
        elif value < root_node.data:
            return self.search(root_node.left, value)
        else:
            return self.search(root_node.right, value)

    def min_value_node(self, root_node):
        current = root_node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root_node, node_value): # Time Complexity is O(lonN) and Space Complexity O(lonN)
        if root_node is None:
            return root_node
        if node_value < root_node.data:
            root_node.left = self.delete_node(root_node.left, node_value)
        elif node_value > root_node.data:
            root_node.right = self.delete_node(root_node.right, node_value)
        else:
            if root_node.left is None:
                temp = root_node.right
                root_node = None
                return temp
            if root_node.right is None:
                temp = root_node.left
                root_node = None
                return temp

            temp = self.min_value_node(root_node.right)
            root_node.data = temp.data
            root_node.right = self.delete_node(root_node.right, temp.data)
        return root_node

    def delete_binary_search_tree(self, root_node):
        root_node.data = None
        root_node.left = None
        root_node.right = None
        return "Binary Search Tree is deleted successfully."

root = TreeNode(None)
binary_search_tree = BinarySearchTree(root)
binary_search_tree.insert_node(root, 70)
binary_search_tree.insert_node(root, 50)
binary_search_tree.insert_node(root, 90)
binary_search_tree.insert_node(root, 30)
binary_search_tree.insert_node(root, 60)
binary_search_tree.insert_node(root, 80)
binary_search_tree.insert_node(root, 100)
binary_search_tree.insert_node(root, 20)
binary_search_tree.insert_node(root, 40)

print("Pre Order Traversal: ", end = " ")
binary_search_tree.pre_order_traversal(root)

print("\nIn Order Traversal: ", end=" ")
binary_search_tree.in_order_traversal(root)

print("\nPost Order Traversal: ", end=" ")
binary_search_tree.post_order_traversal(root)

print("\nLevel Order Traversal: ", end=" ")
binary_search_tree.level_order_traversal(root)

print("\n Searching for element 40.", binary_search_tree.search(root, 40))

binary_search_tree.delete_node(root, 20)
print("\nLevel Order Traversal: ", end=" ")
binary_search_tree.level_order_traversal(root)