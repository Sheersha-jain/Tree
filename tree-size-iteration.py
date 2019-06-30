# Find the size of Tree

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def treesize(node):
    if node is None:
        return
    q = []
    q.append(node)
    size = 0
    while(len(q)):
        node = q[0]
        q.remove(q[0])
        size +=1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return size


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print("size of tree is", treesize(root_node))