# check if existing path of given sum.

class Root:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value

def exixting_path_sum(parent_node, given_sum):
    if parent_node is None:
        return (given_sum ==0)
    else:
        ans  = 0
        print("node", parent_node.key)
        print("now ans",ans)
        current_sum = given_sum- parent_node.key
        print("current sum", current_sum)
        if current_sum==0 and parent_node.right == None and parent_node.left==None:
            return True
        if parent_node.left is not None:
            ans = ans or exixting_path_sum(parent_node.left, current_sum)
        if parent_node.right is not None:
            ans = ans or exixting_path_sum(parent_node.right, current_sum)
        return ans


if __name__ == "__main__":
    root_node = Root(1)
    root_node.left = Root(2)
    root_node.right = Root(3)
    root_node.left.right = Root(55)
    root_node.left.right.left = Root(900)
    print(exixting_path_sum(root_node, 4))