# find total number of leaf node in binary tree.

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def leafnode(parent_node):
    if parent_node is None:
        return
    leaf_node = 0
    q = []
    q.append(parent_node)
    while(len(q)):
        parent_node = q[0]
        if(not parent_node.left and not parent_node.right):
            leaf_node += 1
        q.pop(0)
        if parent_node.left:
            q.append(parent_node.left)
        if parent_node.right:
            q.append(parent_node.right)
    return leaf_node

if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print("total number of leaf nodes are", leafnode(root_node))