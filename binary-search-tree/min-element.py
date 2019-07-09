# Find minimum element in binary tree

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def minelement(parent_node):
    if parent_node is None:
        return 0
    while(parent_node.left is not None):
        parent_node = parent_node.left
    return parent_node.key

if __name__ == "__main__":
    root_node = Root(7)
    root_node.left = Root(4)
    root_node.right = Root(9)
    root_node.left.right = Root(5)
    root_node.left.left = Root(2)
    print(minelement(root_node))