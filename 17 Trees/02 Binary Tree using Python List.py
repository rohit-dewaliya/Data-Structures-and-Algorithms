class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_index = 0
        self.max_size = size
    
    def insert_node(self, value):
        if self.last_index + 1 == self.max_size:
            return "The Binary Tree is full"
        self.custom_list[self.last_index+1] = value
        self.last_index += 1
        return "The value has been successfully inserted"

    def search_node(self, nodeValue):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == nodeValue:
                return "Success"
        return "Not found"
    
    def pre_order_traversal(self, index):
        if index > self.last_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2 + 1)

    def in_order_traversal(self, index):
        if index > self.last_index:
            return
        self.in_order_traversal(index*2)
        print(self.custom_list[index])
        self.in_order_traversal(index*2+1)
    
    def post_order_traversal(self, index):
        if index > self.last_index:
            return
        self.post_order_traversal(index*2)
        self.post_order_traversal(index*2+1)
        print(self.custom_list[index])
    
    def level_order_traversal(self, index):
        for i in range(index, self.last_index+1):
            print(self.custom_list[i])
    
    def delete_node(self, value):
        if self.last_index == 0:
            return "There is not any node to delete"
        for i in range(1, self.last_index+1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_index]
                self.custom_list[self.last_index] = None
                self.last_index -= 1
                return "The node has been successfully deleted"
    
    def delete_binary_tree(self):
       self.custom_list = None
       return "The BT has been successfully deleted"

    
 

newBT = BinaryTree(8)
newBT.insert_node("Drinks")
newBT.insert_node("Hot")
newBT.insert_node("Cold")
newBT.insert_node("Tea")
newBT.insert_node("Coffee")

print(newBT.delete_binary_tree())

newBT.level_order_traversal(1)



