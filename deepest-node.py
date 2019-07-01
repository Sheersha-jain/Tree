# find the deepest node in binary tree.


class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def find(parent_node, level, max_level, res):
    if parent_node is not None:
        level += 1
        find(root_node.left, level, max_level, res)
        if level>max_level:
            res[0] = root_node.key
            max_level[0] = level
        find(root_node.right, level, max_level, res)

def deepestNode(parent_node):
    res = [-1]
    max_level = [-1]
    find(parent_node, 0, max_level, res)
    return res[0]


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)