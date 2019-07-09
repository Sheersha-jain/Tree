# find maximum element in bst using inorder traversal.

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

previous = None

def isbst(parent_node):
    global previous
    previous = None
    return bst_traversal(parent_node)

def bst_traversal(parent_node):
    global previous
    if parent_node is None:
        return True
    if bst_traversal(parent_node.left) is False:
        return False
    if previous is not None and previous.key > parent_node.key:
        return False
    previous = parent_node
    return bst_traversal(parent_node.right)


if __name__ == "__main__":
    root_node = Root(7)
    root_node.left = Root(4)
    root_node.right = Root(9)
    root_node.left.right = Root(5)
    root_node.left.left = Root(200)
    print(isbst(root_node))