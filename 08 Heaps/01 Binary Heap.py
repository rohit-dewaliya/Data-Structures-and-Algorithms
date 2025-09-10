class BinaryHeap():
    def __init__(self, size, heap_type = "MIN"):
        self.custom_list = [None] * (size + 1)
        self.heap_size = 0
        self.max_size = size + 1
        self.heap_type = heap_type

    def peek(self):
        if self.heap_size == 0:
            return None
        return self.custom_list[1]

    def size_of_heap(self):
        return self.heap_size

    def pre_order_traversal(self, index = 1):
        if index > self.heap_size:
            return None
        print(self.custom_list[index], end = ' ')
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)

    def in_order_traversal(self, index = 1):
        if index > self.heap_size:
            return None
        self.in_order_traversal(index * 2)
        print(self.custom_list[index], end = ' ')
        self.in_order_traversal(index * 2 + 1)

    def post_order_traversal(self, index = 1):
        if index > self.heap_size:
            return None
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.custom_list[index], end = ' ')

    def level_order_traversal(self):
        if self.heap_size == 0:
            return None
        for i in range(1, self.heap_size + 1):
            print(self.custom_list[i], end = ' ')
        print()

    def heapify_insert(self, index):
        parent_index = int(index / 2)
        if index <= 1:
            return
        if self.heap_type == "MIN":
            if self.custom_list[index] < self.custom_list[parent_index]:
                temp = self.custom_list[index]
                self.custom_list[index] = self.custom_list[parent_index]
                self.custom_list[parent_index] = temp
            self.heapify_insert(parent_index)
        elif self.heap_type == "MAX":
            if self.custom_list[index] > self.custom_list[parent_index]:
                temp = self.custom_list[index]
                self.custom_list[index] = self.custom_list[parent_index]
                self.custom_list[parent_index] = temp
            self.heapify_insert(parent_index)

    def insert_node(self, value):
        if self.heap_size + 1 == self.max_size:
            return "The Binary Heap is Full"
        self.custom_list[self.heap_size + 1] = value
        self.heap_size += 1
        self.heapify_insert(self.heap_size)
        return "The value has been successfully inserted."

    def heapify_extract(self, index):
        left_index = index * 2
        righ_index = index * 2 + 1
        swap_child = 0

        if self.heap_size < left_index:
            return
        elif self.heap_size == left_index:
            if self.heap_type == "MIN":
                if self.custom_list[index] > self.custom_list[left_index]:
                    temp = self.custom_list[index]
                    self.custom_list[index] = self.custom_list[left_index]
                    self.custom_list[left_index] = temp
                return
            else:
                if self.custom_list[index] < self.custom_list[left_index]:
                    temp = self.custom_list[index]
                    self.custom_list[index] = self.custom_list[left_index]
                    self.custom_list[left_index] = temp
                return
        else:
            if self.heap_type == "MIN":
                if self.custom_list[left_index] < self.custom_list[righ_index]:
                    swap_child = left_index
                else:
                    swap_child = righ_index
                if self.custom_list[index] > self.custom_list[swap_child]:
                    temp = self.custom_list[index]
                    self.custom_list[index] = self.custom_list[swap_child]
                    self.custom_list[swap_child] = temp
            else:
                if self.custom_list[left_index] > self.custom_list[righ_index]:
                    swap_child = left_index
                else:
                    swap_child = righ_index
                if self.custom_list[index] < self.custom_list[swap_child]:
                    temp = self.custom_list[index]
                    self.custom_list[index] = self.custom_list[swap_child]
                    self.custom_list[swap_child] = temp
            self.heapify_extract(swap_child)

    def extract_node(self):
        if self.heap_size == 0:
            return
        extracted_node = self.custom_list[1]
        self.custom_list[1] = self.custom_list[self.heap_size]
        self.custom_list[self.heap_size] = None
        self.heap_size -= 1
        self.heapify_extract(1)
        return extracted_node

    def  delete_enitre_heap(self):
        self.custom_list = None

heap = BinaryHeap(10)
nums = [5, 10, 3, 1, 2]
for num in nums:
    heap.insert_node(num)
heap.level_order_traversal()
heap.extract_node()
heap.level_order_traversal()