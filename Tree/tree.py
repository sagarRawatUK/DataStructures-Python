class TreeNode(object):
    def __init__(self,data):
       self.data = data
       self.children = []
       self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        space = ' '*self.get_level()*3
        prefix = space +  "|--" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p :
            level+=1
            p = p.parent
        return level

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Thinkpad"))

    phone = TreeNode("Phones")
    phone.add_child(TreeNode("iPhone"))
    phone.add_child(TreeNode("Google Pixel"))

    root.add_child(laptop)
    root.add_child(phone)
    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()