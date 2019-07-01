# give an algorithm to delete Tree

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def deletetree(parent_node):
    if parent_node is None:
        return
    deletetree(parent_node.left)
    deletetree(parent_node.right)
    del(parent_node)
    print("Tree Sucessfully Deleted")


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    deletetree(root_node)