'''
Tree is a non-linear data structure with hirarchical relationship between its elements without having a cycle.

Properties-----------#
1. Rerpresent hierarchical data
2. Each node has 2 components: data and link to its sub category
3.

Binary Tree-------------------#
Binary tree is a type of tree data structure in which each node has at most two children, often referred to as left and
right children.

Binary tree is a family of data structure: (BST, Heap Tree, AVL, Red Black Tree, Syntax Tree)

Types of Binary Tree-----#
1. Full Binary Tree: Each node has zero or two children.
2. Perfect Binary Tree: Each non-leaf node have two children and at the same depth.
3. Complete Binary Tree: Each node has two children except the last nodes
4. Balanced Binary Tree: Each leaf node is located at the same distance from the root node.

Traversal of Binary Tree-----------#
1. Depth first Search
    a. PreOrder Traversal
    b. Inorder Traversal
    c. Post Order Traversal
2. Breadth First Search
    a. Level Order Traversal
'''
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def pre_order_traversal(self, node):
        if not node:
            return
        print(node.data)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if not node:
            return
        self.in_order_traversal(node.left)
        print(node.data)
        self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if not node:
            return
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(node.data)

    def level_order_traversal(self):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search_node(self, node_vaue):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.data == node_vaue:
                return "Node Found"
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return "Node not found."

    def insert_new_node(self, new_node):
        if not self.root:
            self.root = new_node
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            else:
                node.left = new_node
                return "Successfully Added the New Node"
            if node.right:
                queue.append(node.right)
            else:
                node.right = new_node
                return "Successful Added the New Node"

    def get_deepest_node(self):
        if not self.root:
            return None

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return node

    def delete_deepest_node(self, node_to_delete):
        if not self.root:
            return None

        queue = deque([self.root])

        while queue:
            current_node = queue.popleft()

            if current_node.left:
                if current_node.left is node_to_delete:
                    current_node.left = None  # Remove the node
                    return
                queue.append(current_node.left)

            if current_node.right:
                if current_node.right is node_to_delete:
                    current_node.right = None  # Remove the node
                    return
                queue.append(current_node.right)

    def delete_node(self, node):
        if self.root is None:
            return None
        else:
            queue = deque([self.root])

            while queue:
                current_node = queue.popleft()
                if current_node.data == node:
                    delete_node = self.get_deepest_node()
                    current_node.data = delete_node.data
                    self.delete_deepest_node(delete_node)
                    return "Successfully deleted the node."
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return "Failed to delete the node."

    def delete_binary_tree(self):
        self.root.data = None
        self.root.left = None
        self.root.right = None
        return "Binary tree deleted successfully."

new_binary_tree = TreeNode('Drinks')
new_left_child = TreeNode('Hot')
new_right_child = TreeNode('Cold')

new_binary_tree.left = new_left_child
new_binary_tree.right = new_right_child

new_left_child_1 = TreeNode('Chai')
new_right_child_1 = TreeNode('Coffee')
new_left_child.left = new_left_child_1
new_left_child.right = new_right_child_1

new_left_child_2 = TreeNode('Non Alcoholic')
new_right_child_2 = TreeNode('Alcoholic')
new_right_child.left = new_left_child_2
new_right_child.right = new_right_child_2

tree = BinaryTree(new_binary_tree)
print("\n", "Pre Order Traversal")
tree.pre_order_traversal(new_binary_tree)
print("\n", "In Order Traversal")
tree.in_order_traversal(new_binary_tree)
print("\n", "Post Order Traversal")
tree.post_order_traversal(new_binary_tree)
print("\n", "Level Order Traversal")
tree.level_order_traversal()
print(tree.search_node('Chai'))
new_node = TreeNode('Cola')
tree.insert_new_node(new_node)
tree.level_order_traversal()

print(tree.delete_node('Coffee'))
print("\n")
tree.level_order_traversal()
print(tree.delete_binary_tree())