# print all the path from root to leaf of binary tree.

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def printpath(parent_node):
    path = []
    printpathtrail(parent_node, path, 0)

def printpathtrail(parent_node, path, path_length):
    if parent_node is None:
        return 0
    if len(path)>path_length:
        path[path_length]=parent_node.key
    else:
        path.append(parent_node.key)
    path_length += 1
    if parent_node.left is None and parent_node.right is None:
        printfinalpath(path, path_length)
    else:
        printpathtrail(parent_node.left, path, path_length)
        printpathtrail(parent_node.right, path, path_length)

def printfinalpath(ints, len):
    for i in ints[0:len]:
        print(i, " ", end="")
    print()

if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print(printpath(root_node))