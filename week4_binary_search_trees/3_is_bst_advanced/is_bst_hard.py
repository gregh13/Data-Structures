#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


def is_bst(tree, nodes):
    def check_inorder(key_index, parent):
        parents[key_index] = parent

        # Check if null child node
        if key_index == -1:
            return

        # Store value for use below; node = [node value, left child index, right child index]
        node = tree[key_index]

        # Traverse inorder, check left child first
        check_inorder(node[1], key_index)

        # Check that tree is inorder (i.e. ascending in value)
        if node[0] > results[-1]:
            # Node value in order, add current node value to list
            results.append(node[0])
        else:
            if node[0] == results[-1]:
                # Need to make sure same value wasn't from parent's left child (assignment stipulations)
                parent_node = tree[parent]
                left_child_index = parent_node[1]
                if left_child_index == key_index:
                    pass
            else:
                # Found value not in order, change flag
                correct_tree[0] = False
                return

        # Check right child
        check_inorder(node[2], key_index)

        return

    # Initialize parent node array
    parents = [-1 for _ in range(nodes)]

    # Initialize results, start with negative infinity for first leaf value comparison
    results = [float("-inf")]

    # Initialize answer flag as list for easier access within recursive function
    correct_tree = [True]

    # Start search with root index
    check_inorder(0, -1)

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
        if is_bst(tree, nodes):
            print("CORRECT")
        else:
            print("INCORRECT")
    else:
        print("CORRECT")


threading.Thread(target=main).start()
