'''
an AVL tree is an self-balancing binary search tree where the difference between heights of left and right subtrees
cannot be more than one for all nodes.

Common Operation:
    - creation
    - serach
    - traverse
        - preorder
        - inorder
        - postorder
        - level order
    - insertion
        - CASE I: Rotation is not required
        - CASE II: Rotation is required
            -: Left Left Condition -> Rotate the whole tree to right from the point of disbalance tree
            -: Left Right Condition -> Rotate the whole tree to left from the point of disbalance tree and then it will
                                        becomes the Left Left Condition
            -: Right Right Condition -> Rotate the whole tree to left from the point of disbalance tree
            -: Right Left Condition -> Rotate the whole tree to right from the point of disbalance tree and then it will
                                        becomes the Right Right Condition
    - deletion of node
        - CASE I: Rotation is not required
            -: deleted node has not child
            -: deleted node has one child
            -: deleted node has two children
        - CASE II: Rotation is required
            -: Left Left Condition -> Rotate the whole tree to right from the point of disbalance tree
            -: Left Right Condition -> Rotate the whole tree to left from the point of disbalance tree and then it will
                                        becomes the Left Left Condition
            -: Right Right Condition -> Rotate the whole tree to left from the point of disbalance tree
            -: Right Left Condition -> Rotate the whole tree to right from the point of disbalance tree and then it will
                                        becomes the Right Right Condition
    - deletion of entire tree
'''

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self, root):
        self.root = root

    def preorder(self, root):
        if root is None:
            return None
        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)
        return

    def inorder(self, root):
        if root is None:
            return None
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)
        return

    def postorder(self, root):
        if root is None:
            return None
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=' ')
        return

    def level_order(self, root):
        if root is None:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value(root.left)

    def rotate_right(self, disbalance_node):
        new_root = disbalance_node.left
        temp = new_root.right

        new_root.right = disbalance_node
        disbalance_node.left = temp

        disbalance_node.height = 1 + max(self.get_height(disbalance_node.left), self.get_height(disbalance_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def rotate_left(self, disbalance_node):
        new_root = disbalance_node.right
        temp = new_root.left

        new_root.left = disbalance_node
        disbalance_node.right = temp

        disbalance_node.height = 1 + max(self.get_height(disbalance_node.left), self.get_height(disbalance_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def insert_node(self, root, value):
        if not root:
            return AVLNode(value)
        elif value < root.data:
            root.left = self.insert_node(root.left, value)
        elif value > root.data:
            root.right = self.insert_node(root.right, value)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and value < root.left.data:
            return self.rotate_right(root)
        if balance > 1 and value > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and value > root.right.data:
            return self.rotate_left(root)
        if balance < -1 and value < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete_node(self, root, value):
        if not root:
            return AVLNode(value)
        elif value < root.data:
            root.left = self.delete_node(root.left, value)
        elif value > root.data:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete_entire_tree(self, root):
        root.data = None
        root.left = None
        root.right = None
        root.height = 0
        return "AVL Tree has successfully deleted"

nums = [1, 2, 3, 4, 5, 6, 7]
tree_root = AVLNode(nums[0])
avl_tree = AVLTree(-1)
for num in nums:
    if num != nums[0]:
        tree_root = avl_tree.insert_node(tree_root, num)
    avl_tree.level_order(tree_root)
    print()
print("Level Order Traversal: ", end = " ")
avl_tree.level_order(tree_root)
print("\nPre Order Traversal: ", end = " ")
avl_tree.preorder(tree_root)
print("\nIn Order Traversal: ", end = " ")
avl_tree.inorder(tree_root)
print("\nPost Order Traversal: ", end = " ")
avl_tree.postorder(tree_root)
print("\n\nDeleting the 20 Node")
avl_tree.delete_node(tree_root, 4)
avl_tree.level_order(tree_root)