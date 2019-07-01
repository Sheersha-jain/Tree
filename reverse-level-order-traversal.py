class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def reverse_level_order(root_node):
    if root_node is None:
        return
    q = []
    s = []
    q.append(root_node)
    while(len(q)):
        root_node = q.pop(0)
        s.append(root_node)
        if root_node.right:
            q.append(root_node.right)
        if root_node.left:
            q.append(root_node.left)

    while(len(s)):
        root_node = s.pop()
        print(root_node.key)



if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    reverse_level_order(root_node)