class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


root = TreeNode("Electronics")
laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("mac"))
laptop.add_child(TreeNode("HP"))
laptop.add_child(TreeNode("Dell"))

root.add_child(laptop)
laptop.parent = root

root.print_tree()
