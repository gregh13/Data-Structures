from sys import stdin

# Splay tree implementation


# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        self.key, self.sum, self.left, self.right, self.parent = key, sum, left, right, parent


def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v


def small_rotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    else:
        # Zig-zag
        small_rotation(v)
        small_rotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return next, root


def split(root, key):
    result, root = find(root, key)
    if result is None:
        return root, None
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return left, right


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    # print("-------\n")
    # print("Insert: ", x)
    # if root is not None:
    # #     print("root: ", root.key, root.parent, root.left, root.right, root.sum)
    # print_tree("in", root, "Before Insert (inorder): ")
    # print_tree("post", root, "Before Insert (post order): ")
    new_vertex = Vertex(x, x, None, None, None)
    if root is None:
        # First vertex of tree
        root = new_vertex
        return
    # print_tree("post", root, "Before Insert 1st Find (post order): ")

    parent, root = find(root, x)

    # print_tree("in", root, "After Insert 1st Find (inorder): ")
    # print_tree("post", root, "After Insert 1st Find (post order): ")

    if parent is None:
        # x is larger than any key in set. find(root, x) splayed last biggest key to root
        # if root.right is not None:
        #     print("Insert: Right child not None!")
        root.right = new_vertex
        new_vertex.parent = root
        update(root)
    elif x < parent.key:
        left_child = parent.left
        # if left_child is not None:
            # print("Insert: Left child not None!")
        parent.left = new_vertex
        new_vertex.parent = parent
        new_vertex.left = left_child
        update(new_vertex)
        update(parent)
    elif x > parent.key:
        # if parent.right is not None:
            # print("Insert: Right child not None!")
        parent.right = new_vertex
        new_vertex.parent = parent
        update(new_vertex)
        update(parent)
    else:
        # Already in tree, don't need to insert
        pass

    _, root = find(root, x)

    # print_tree("in", root, "After Insert 2nd Find (inorder): ")
    # print_tree("post", root, "After Insert 2nd Find (post order): ")


    return


# def insert(x):
#     global root
#     left, right = split(root, x)
#     new_vertex = None
#     if right is None or right.key != x:
#         new_vertex = Vertex(x, x, None, None, None)
#     root = merge(merge(left, new_vertex), right)


def remove(v):
    global root
    parent = v.parent

    if parent is None:
        # Removing the root vertex
        # Vertex doesn't have a right child (see delete_vertex), so just make v.left new root (if any)
        if v.left is not None:
            root = v.left
            root.parent = None
        else:
            root = None

    elif v.left is None:
        # v is a leaf, easy delete
        if v.key < parent.key:
            parent.left = None

        else:
            parent.right = None

        update(parent)
    else:
        # promote v.left
        v_left_child = v.left
        v_left_child.parent = parent
        if v_left_child.key < parent.key:
            parent.left = v_left_child
        else:
            parent.right = v_left_child

        update(parent)

    del v


def delete_vertex(v):
    global root
    # print_tree("in", root, "Before Delete (inorder): ")
    # print_tree("post", root, "Before Delete (post order): ")
    if v.right is None:
        # print("REMOVE")
        remove(v)
    else:
        # print("NEXT_BIGGEST")
        next_biggest, root = find(root, v.key + 1)
        # Bring vertex to delete back to top (should just be one case of zig)
        # print_tree("post", root, "Before Delete Splay (post order): ")
        root = splay(v)
        # print_tree("post", root, "After Delete Splay (post order): ")
        # if next_biggest.left is not None:
            # print("Delete: Left child is not None!")
        # Replace v with next_biggest
        v.key = next_biggest.key
        # print("Next Biggest Key: ", next_biggest.key)
        # Maybe need to update from bottom up?? Possible call splay on next_biggest? Already did above???

        # Promote next_biggest.right (if any)
        if next_biggest.right is None:
            # Nothing to promote
            # print("No Promo")
            v.right = None
            pass
        else:
            # print("PROMOTION")
            parent = next_biggest.parent
            promoted_right = next_biggest.right
            promoted_right.parent = parent
            if promoted_right.key < parent.key:
                parent.left = promoted_right
            else:
                parent.right = promoted_right

        update(v)

        del next_biggest

    # print_tree("in", root, "After Delete (inorder): ")
    # print_tree("post", root, "After Delete (post order): ")


def erase(x):
    global root
    # print("-------\n")
    # print("Erase: ", x)
    # if root is not None:
    # #     print("root: ", root.key, root.parent, root.left, root.right, root.sum)
    # print_tree("in", root, "Before Erase (inorder): ")
    # print_tree("post", root, "Before Erase (post order): ")
    result, root = find(root, x)
    if result is None:
        # x is larger than any element in tree, no next value
        return
    if result.key == x:
        # Key is in tree, need to delete_vertex
        find(root, x+1)
        root = splay(result)
        delete_vertex(result)
    else:
        # Key isn't in tree, nothing to delete
        pass
    # print_tree("in", root, "After Erase (inorder): ")
    # print_tree("post", root, "After Erase (post order): ")


def search(x):
    global root
    # print("-------\n")
    # print("Search: ", x)
    # if root is not None:
    # #     print("root: ", root.key, root.parent, root.left, root.right, root.sum)
    # print_tree("in", root, "Before Search (inorder): ")
    # print_tree("post", root, "Before Search (post order): ")
    result, root = find(root, x)
    # print_tree("in", root, "After Search (inorder): ")
    # print_tree("post", root, "After Search (post order): ")
    if root is not None:
        if root.key == x:
            return True
    if result is None:
        return False
    if result.key == x:
        return True
    else:
        return False


def range_sum(start, end):
    global root
    # print("-------\n")
    # print(f"Sum Range: {start} to {end}")
    # if root is not None:
    # #     print("root: ", root.key, root.parent, root.left, root.right, root.sum)
    # print_tree("in", root, "Before SUM (inorder): ")
    # print_tree("post", root, "Before SUM (post order): ")

    # print_tree("in", root, "After SUM (inorder): ")
    # print_tree("post", root, "After SUM (post order): ")

    left_subtrahend = 0
    right_subtrahend = 0
    total_sum = 0

    if root is None:
        # No tree
        return total_sum

    start_result, root = find(root, start)

    if start_result is None:
        # All keys in tree are smaller than range start
        return total_sum

    total_sum = root.sum

    if start_result.key > root.key:
        total_sum = start_result.sum
    else:
        # start_result is root and its key == start
        if start_result.left is not None:
            left_subtrahend = start_result.left.sum

    # Update total sum
    total_sum = total_sum - left_subtrahend

    end_result, root = find(root, end)

    if end_result is None:
        # No key in tree is larger than range end
        return total_sum

    if root.key > end:
        # End is in between nodes, root.key is next largest (out of range)
        if root.left is not None:
            right_subtrahend = root.sum - root.left.sum
    else:
        # root.key == end
        if root.right is not None:
            right_subtrahend = root.right.sum

    total_sum = total_sum - right_subtrahend

    return total_sum


# def sum(fr, to):
#     global root
#     left, middle = split(root, fr)
#     middle, right = split(middle, to + 1)
#     ans = 0
#     # Complete the implementation of sum
#
#     return ans


def print_tree(order, v, placement):
    def get_inorder(vertex):
        # Check if null child node
        if vertex is None:
            return

        # Traverse to left child, then parent, then right child
        get_inorder(vertex.left)
        results.append(vertex.key)
        get_inorder(vertex.right)
        return

    def get_postorder(vertex):
        # Check if null child node
        if vertex is None:
            return

        # Traverse to left child, then parent, then right child
        get_inorder(vertex.left)
        get_inorder(vertex.right)
        results.append(vertex.key)
        return

    results = []
    if order == "in":
        get_inorder(v)
    elif order == "post":
        get_postorder(v)
    else:
        results = ["You forgot to add the order parameter!"]

    print(placement, *results)
    return


# print("\n\n-----------------------------------------------------------------------------\n\n")
MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = range_sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
