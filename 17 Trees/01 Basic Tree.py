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

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
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


new_binary_tree = BinaryTree('Drinks')
new_left_child = BinaryTree('Hot')
new_right_child = BinaryTree('Cold')

new_binary_tree.left = new_left_child
new_binary_tree.right = new_right_child

new_left_child_1 = BinaryTree('Chai')
new_right_child_1 = BinaryTree('Coffee')
new_left_child.left = new_left_child_1
new_left_child.right = new_right_child_1

new_left_child_2 = BinaryTree('Non Alcoholic')
new_right_child_2 = BinaryTree('Alcoholic')
new_right_child.left = new_left_child_2
new_right_child.right = new_right_child_2

tree = Tree(new_binary_tree)
print("\n", "Pre Order Traversal")
tree.pre_order_traversal(new_binary_tree)
print("\n", "In Order Traversal")
tree.in_order_traversal(new_binary_tree)
print("\n", "Post Order Traversal")
tree.post_order_traversal(new_binary_tree)
print("\n", "Level Order Traversal")
tree.level_order_traversal()