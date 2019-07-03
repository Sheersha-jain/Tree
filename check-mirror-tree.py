# Given two binary tree check if they are mirror

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def check_mirror_tree(parent_nodeA, parent_nodeB):
    if parent_nodeA is None and parent_nodeB is None:
        return True
    if parent_nodeA is None or parent_nodeB is None:
        return False

    else:
        return parent_nodeA.key==parent_nodeB.key and \
        check_mirror_tree(parent_nodeA.left, parent_nodeB.right) and \
        check_mirror_tree(parent_nodeA.right, parent_nodeB.left)


if __name__ == "__main__":
    root1 = Root(1)
    root2 = Root(1)

    root1.left = Root(2)
    root1.right = Root(3)
    root1.left.left = Root(4)
    root1.left.right = Root(5)

    root2.left = Root(3)
    root2.right = Root(2)
    root2.right.left = Root(5)
    root2.right.right = Root(4)

    if check_mirror_tree(root1, root2):
        print ("Yes")
    else:
        print ("No")
