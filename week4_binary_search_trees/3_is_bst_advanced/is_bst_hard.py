#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


def is_bst(tree):
    def check_inorder(key_index):
        # Check if null child node
        if key_index == -1 or not correct_tree[0]:
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
            # Check if it's a duplicate
            if node[0] == results[-1]:
                # Left side is strictly less than node value, so when two values are the same, it must go to the right
                # As such, the duplicate node won't have a left child since any value would break the tree conditions
                if node[1] == -1:
                    # No left child, duplicate node is in proper place
                    results.append(node[0])
                else:
                    # Duplicate is somewhere to the left of current value, proper order is broken
                    correct_tree[0] = False
                    return
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
    # Number of nodes
    nodes = int(sys.stdin.readline().strip())

    # Initialize empty tree
    tree = []

    # Build tree
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    # Check if tree exists
    if len(tree) > 0:

        # Check if tree is a valid binary search tree
        if is_bst(tree):
            print("CORRECT")
        else:
            print("INCORRECT")
    else:
        print("CORRECT")


threading.Thread(target=main).start()
