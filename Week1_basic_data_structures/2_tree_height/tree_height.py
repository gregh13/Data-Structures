# import sys
# import threading


class Node:
    def __init__(self):
        self.children = []
        self.level = None

    def add_child(self, child):
        self.children.append(child)


def build_tree(n, parents):

    # Initialize root value
    root = None

    # Initialize node array with blank, unique Nodes
    node_array = [Node() for x in range(n)]

    # Assignment input has a list of values (parents). The index value in the list is their own index (the child_index)
    for child_index in range(n):

        # The value that is stored at the child_index is their parent's index in the list
        parent_index = parents[child_index]

        # Per assignment stipulations, input list contains exactly one root, marked by a value of -1
        if parent_index == -1:
            root = child_index
        else:
            # Update parent node's children with the child node object
            node_array[parent_index].add_child(node_array[child_index])

    # Return root node
    return node_array[root]


def find_height(root):
    if root is None:
        return 0

    # Initialize root level and set as node
    node = root
    node.level = 1

    # Initialize queue, enqueue root node
    queue_array = [node]

    while queue_array:
        # Dequeue
        node = queue_array.pop(0)

        # Update each child node's level
        for child in node.children:
            child.level = node.level + 1
            queue_array.append(child)

    # Either returns most recent node level
    return node.level


def compute_height_naive(n, parents):
    # Starter algorithm, naive approach
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
    # print(compute_height_naive(n, parents))
    root = build_tree(n, parents)
    print(find_height(root))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()

if __name__ == "__main__":
    main()
