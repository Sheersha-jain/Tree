# Find a element in a binary tree interation.


class Root:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

def findelement(node, node_to_find):
    if node is None:
        return
    q = []
    q.append(node)
    while(len(q)>0):
        node = q[0]
        if node.key == node_to_find:
            return "found"
        else:
            if node.left is not None:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            q.remove(q[0])

    return "node not present"

def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.key)
    inorder(temp.right)


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    x= findelement(root_node, 200)
    print(x)