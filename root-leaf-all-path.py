# print all paths from root to leaf of a binary tree.

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def findallpath(q, parent_node):
    if parent_node == None:
        return
    q.append(parent_node.key)
    if(parent_node.left is None and parent_node.right is None):
        for i in range(len(q)):
            print(q)
    findallpath(q, parent_node.left)
    findallpath(q, parent_node.right)
    q.pop()


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    findallpath([], root_node)