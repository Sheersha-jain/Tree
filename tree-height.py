# Algorithm to find Height of tree.

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def treeheight(parent_node):
    if parent_node is None:
        return 0
    left_subtree_height = treeheight(parent_node.left)
    right_subtree_height = treeheight(parent_node.right)
    if (left_subtree_height > right_subtree_height):
        return  left_subtree_height +1
    else:
        return right_subtree_height +1

if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print("height of the Tree is",treeheight(root_node))