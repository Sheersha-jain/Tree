# Find maximum element in Binary tree using Iteration

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def maxelement(node):
    if node is None:
        return
    max_node = 0
    q =[]
    q.append(node)
    while(len(q)):
        node = q[0]
        if node.key > max_node:
            max_node = node.key
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        q.remove(node)
    return max_node


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    x = maxelement(root_node)
    print(x)