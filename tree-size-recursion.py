# Find the size of tree using recursion

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def treesize(node):
    if node is None:
        return 0
    else:
        return treesize(node.left)+ 1 + treesize(node.right)

if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print("size of tree is", treesize(root_node))