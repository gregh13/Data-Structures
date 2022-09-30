# python3

import sys
import threading


class Node:
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def build_tree(n, parents):

    node_array = [Node] * n

    for child_index in range(len(n)):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            node_array[parent_index].add_child(node_array[child_index])

    find_height(root)


def find_height(root):
    if not root:
        return 0

    queue_array = [root]
    height = 0
    while queue_array:
        node = queue_array.pop(0)
        queue_array.append(*node.children)

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    build_tree(n, parents)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

if __name__ == "__main__":
    main()
