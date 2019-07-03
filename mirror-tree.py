# Convert a tree into its mirror tree.

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def mirror_tree(parent_node):
    if parent_node is None:
        return 0
    if parent_node:
        mirror_tree(parent_node.left)
        mirror_tree(parent_node.right)
        temp = parent_node.left
        parent_node.left = parent_node.right
        parent_node.right = temp
    print(parent_node.key)

if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print(mirror_tree(root_node))