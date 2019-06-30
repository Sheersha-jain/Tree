# find the maximum element in binary tree using recursion.


class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def maxelement(node):
    if node is None:
        return -99999

    root_data = node.key

    left_max = maxelement(node.left)
    right_max = maxelement(node.right)

    if (left_max > root_data):
        root_data = left_max
    if  (right_max != None and right_max > root_data):
        root_data = right_max
    return root_data

if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print("Maximum element is",maxelement(root_node))