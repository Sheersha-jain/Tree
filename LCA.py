# given two nodes find theor lowest common ancestor


class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def LCA(parent_node, a, b):
    if parent_node is None:
        return 0
    if parent_node.key is a or parent_node.key is b:
        return parent_node.key

    left_lca = LCA(parent_node.left, a, b)
    right_lca = LCA(parent_node.right, a, b)
    if left_lca or right_lca:
        return parent_node.key
    return left_lca if left_lca is not None else right_lca


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.left = Root(900)
    print(LCA(root_node, 55, 900))
