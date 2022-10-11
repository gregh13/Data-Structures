# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.results = []
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inorder(self):
        def get_inorder(key_index):
            if self.left[key_index] == -1:
                self.results.append(self.key[key_index])
                if self.right[key_index] != -1:
                    get_inorder(self.right[key_index])
                return

            get_inorder(self.left[key_index])
            self.results.append(self.key[key_index])
            if self.right[key_index] != -1:
                get_inorder(self.right[key_index])

            return

        self.results = []
        # Start search with root index
        get_inorder(0)

        return self.results

    def preorder(self):
        self.results = []

        return self.results

    def postorder(self):
        self.results = []

        return self.results



def main():
    tree = TreeOrders()
    print(" ".join(str(x) for x in tree.inorder()))
    print(" ".join(str(x) for x in tree.preorder()))
    print(" ".join(str(x) for x in tree.postorder()))


threading.Thread(target=main).start()
