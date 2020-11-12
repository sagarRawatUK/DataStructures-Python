class BSTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return

        if data<self.data:
            # add data to left 
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTreeNode(data)
        else:
            # add value to right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTreeNode(data)

    def search(self,value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def in_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements+= self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements+= self.right.in_order_traversal()
        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.right
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data+left_sum+right_sum
            



def build_tree(elements):
        root = BSTreeNode(elements[0])
        for i in range(1,len(elements)):
            root.add_child(elements[i])
        return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build_tree(numbers)
    print(tree.in_order_traversal())
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())