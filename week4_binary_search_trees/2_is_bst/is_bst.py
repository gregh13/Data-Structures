#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


def is_bst(tree):
    def check_inorder(key_index):
        if key_index == -1:
            return

        node = tree[key_index]
        check_inorder(node[1])
        if node[0] > results[-1]:
            results.append(node[0])
        else:
            okay_tree[0] = False
            return
        check_inorder(node[2])

        return

    # Reset results list
    results = [float("-inf")]
    okay_tree = [True]
    # Start search with root index
    check_inorder(0)
    return okay_tree[0]


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
