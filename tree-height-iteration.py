# find height of binary tree using Iteration

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def treeheight(parent_node):
    if parent_node is None:
        return 0
    q = []
    q.append(parent_node)
    height = 0
    while(True):
        node_count = len(q)
        if node_count == 0:
            return height
        height += 1

        while(node_count > 0):
            parent_node = q[0]
            q.pop(0)
            if parent_node.left:
                q.append(parent_node.left)
            if parent_node.right:
                q.append(parent_node.right)
            node_count -= 1

if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print("height of tree is",treeheight(root_node))