class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value


if __name__ == "__main__":
    root_node = Root(7)
    root_node.left = Root(4)
    root_node.right = Root(9)
    root_node.left.right = Root(5)
    root_node.left.left = Root(2)