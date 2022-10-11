# python3

import sys, threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        # Initialize input variables and results list
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.results = []

        # Read input into appropriate arrays (i.e. build the binary tree input)
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inorder(self):
        def get_inorder(key_index):
            # Check if null child node
            if key_index == -1:
                return

            # Traverse to left child, then parent, then right child
            get_inorder(self.left[key_index])
            self.results.append(self.key[key_index])
            get_inorder(self.right[key_index])

            return

        # Reset results list
        self.results = []
        # Start search with root index
        get_inorder(0)

        return self.results

    def preorder(self):
        def get_preorder(key_index):
            # Check if null child node
            if key_index == -1:
                return

            # Traverse to parent, then left child, then right child
            self.results.append(self.key[key_index])
            get_preorder(self.left[key_index])
            get_preorder(self.right[key_index])

            return

        # Reset results list
        self.results = []
        # Start search with root index
        get_preorder(0)
        return self.results

    def postorder(self):
        def get_postorder(key_index):
            # Check if null child node
            if key_index == -1:
                return

            # Traverse to right child, then left child, then to parent
            get_postorder(self.left[key_index])
            get_postorder(self.right[key_index])
            self.results.append(self.key[key_index])

            return

        # Reset results list
        self.results = []
        # Start search with root index
        get_postorder(0)
        return self.results



def main():
    tree = TreeOrders()
    print(" ".join(str(x) for x in tree.inorder()))
    print(" ".join(str(x) for x in tree.preorder()))
    print(" ".join(str(x) for x in tree.postorder()))


threading.Thread(target=main).start()
