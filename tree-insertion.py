#  Insertion in binary tree


class Root:
    def __init__(self, value):
         self.left = None
         self.right = None
         self.key = value

def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.key)
    inorder(temp.right)

def insert(temp, key):
    if not temp:
        return
    q = []
    q.append(temp)
    while(len(q)):
        temp = q[0]
        q.pop(0)
        if(not temp.left):
            temp.left = Root(key)
            break
        else:
            q.append(temp.left)
        if(not temp.right):
            temp.right = Root(key)
            break
        else:
            q.append(temp.right)

if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)

    print("Tree before traversal")
    inorder(root_node)

    print("Tree after Insertion of node")
    insert(root_node, 22)
    inorder(root_node)

