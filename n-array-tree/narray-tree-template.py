class Nroot:
    def __init__(self, value):
        self.data = value
        self.first_child = None
        self.next_sibling = None


if __name__ == "__main__":
    nroot = Nroot(1)
    nroot.first_child = Nroot(2)
    nroot.first_child.next_sibling = Nroot(3)
    nroot.first_child.first_child = Nroot(4)
    nroot.first_child.next_sibling.first_child = Nroot(5)