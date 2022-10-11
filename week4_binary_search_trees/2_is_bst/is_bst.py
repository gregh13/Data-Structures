#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


def is_bst(tree):
    def check_inorder(key_index):
        # Check if null child node
        if key_index == -1:
            return

        # Store value for use below; node = [node value, left child index, right child index]
        node = tree[key_index]

        # Traverse inorder, check left child first
        check_inorder(node[1])

        # Check that tree is inorder (i.e. ascending in value)
        if node[0] > results[-1]:
            # Node value in order, add current node value to list
            results.append(node[0])
        else:
            # Found value not in order, change flag
            correct_tree[0] = False
            return

        # Check right child
        check_inorder(node[2])

        return

    # Initialize results, start with negative infinity for first leaf value comparison
    results = [float("-inf")]

    # Initialize answer flag as list for easier access within recursive function
    correct_tree = [True]

    # Start search with root index
    check_inorder(0)

    return correct_tree[0]


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if len(tree) > 0:
        if is_bst(tree):
            print("CORRECT")
        else:
            print("INCORRECT")
    else:
        print("CORRECT")


threading.Thread(target=main).start()
