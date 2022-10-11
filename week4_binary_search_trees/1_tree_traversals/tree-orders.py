# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.result = []
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
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
                
        return self.result

    def preorder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
                
        return self.result

    def postorder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result


def main():
    tree = TreeOrders()
    print(" ".join(str(x) for x in tree.inorder()))
    print(" ".join(str(x) for x in tree.preorder()))
    print(" ".join(str(x) for x in tree.postorder()))


threading.Thread(target=main).start()
