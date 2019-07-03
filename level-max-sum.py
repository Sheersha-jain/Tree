# Find the level which has maximum sum in binary tree


class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def max_level_sum(parent_node):
    if parent_node is None:
        return 0
    q = []
    q.append(parent_node)
    level_max = 0
    while(True):
        current_max =0
        node_count = len(q)
        if node_count ==0:
            return level_max
        while(node_count):
            parent_node = q[0]
            current_max += parent_node.key
            if current_max > level_max:
                level_max = current_max
            q.pop(0)
            node_count -=1
            if parent_node.left:
                q.append(parent_node.left)
            if parent_node.right:
                q.append(parent_node.right)


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    root_node.left.right.right = Root(88)
    root_node.left.right.right.left = Root(1000)
    root_node.left.right.right.right = Root(1000)
    print(max_level_sum(root_node))