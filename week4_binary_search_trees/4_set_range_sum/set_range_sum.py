from sys import stdin


# ---------------------------------------------------------------------------------------------------- #
# Splay tree implementation


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


# ---------------------------------------------------------------------------------------------------- #
# Code that uses splay tree to solve the problem


def insert(x):
    global root

    # Initialize new vertex
    new_vertex = Vertex(x, x, None, None, None)

    if root is None:
        # First vertex of tree
        root = new_vertex
        return

    # Check if x is in tree and if not, where to put it
    parent, root = find(root, x)

    if parent is None:
        # x is larger than any key in set. find(root, x) splayed last biggest key to root, so can just add it to right
        root.right = new_vertex
        new_vertex.parent = root

    elif x < parent.key:
        # Add x as parent's left child, reattach original left child to new vertex
        left_child = parent.left
        parent.left = new_vertex
        new_vertex.parent = parent
        new_vertex.left = left_child

    else:
        # Already in tree, don't need to insert anything
        pass

    # Find newly inserted vertex to update all vertex sums affected by insertion
    _, root = find(root, x)

    return


def erase(x):
    global root

    # Check if x is in tree
    result, root = find(root, x)

    if result is None:
        # x is larger than any element in tree, no next value
        return
    if result.key == x:
        # Key is in tree, need to delete_vertex

        # First find next largest (i.e. the replacement vertex)
        next_largest, root = find(root, x+1)

        # Then move vertex to delete back to root (in case x+1 is in tree, it would have been splayed to root)
        root = splay(result)

        # Call delete function now that vertex is the root and it's replacement has been splayed near top
        delete_vertex(next_largest)

    else:
        # Key isn't in tree, nothing to delete
        pass


def delete_vertex(replacement):
    global root

    if replacement is None:
        # No next largest number, means that key to delete is largest in set
        remove_largest(root)

    else:
        # Replace root with next largest
        root.key = replacement.key

        # Promote replacement.right (if any)
        if replacement.right is not None:
            # Need to promote
            promoted_right = replacement.right
            promoted_right.parent = root
            root.right = promoted_right

        else:
            # Nothing to promote, update root accordingly
            root.right = None
            pass

        # Update sum values after deletion
        update(root)

        # Remove vertex object from memory
        del replacement


def remove_largest(v):
    global root

    # Vertex to remove is currently root and has no right child. Need to check if it has a left child
    if root.left is not None:
        # Make left child the root
        root = root.left
        root.parent = None
    else:
        # No left child, meaning it was the only vertex in tree, now empty tree
        root = None

    # Remove vertex object from memory
    del v


def search(x):
    global root

    result, root = find(root, x)

    if root is not None:
        if root.key == x:
            return True
        else:
            return False

    else:
        # Empty tree
        return False


def range_sum(start, end):
    global root

    # Initialize sum calculation variables
    left_subtrahend = 0
    right_subtrahend = 0
    total_sum = 0

    if root is None:
        # Empty tree
        return total_sum

    # Search for first vertex in tree with a key within the sum range query
    start_result, root = find(root, start)

    if start_result is None:
        # All keys in tree are smaller than range start
        return total_sum

    # Store key into value for use below
    start_result_val = start_result.key

    # Check if first key found in tree after beginning of range is within the end bound
    if start_result_val >= end:
        if start_result_val == end:
            # Just one vertex in range
            total_sum = start_result_val
            return total_sum
        else:
            # Range is too small, no keys inside
            return total_sum

    # Root sum will always be the total of all key values in the tree
    total_sum = root.sum

    # If first vertex within the range is not the root, make it the root
    if root.key < start_result_val:
        root = splay(start_result)

    # Check for any vertices that are smaller than the start range (and thus need to be excluded from total sum)
    if root.left is not None:
        left_subtrahend = root.left.sum

    # Update total sum (remove keys before range start)
    total_sum = total_sum - left_subtrahend

    # Search for last vertex within sum range
    end_result, root = find(root, end)

    if end_result is None:
        # No key in tree is larger than range end, so don't need to subtract anything from right bound
        return total_sum

    if root.key > end:
        # End is in between nodes, root.key is next largest (out of sum range)
        if root.left is not None:
            # Get sum of key that are bigger than end range, need to subtract it from total sum (including root key)
            right_subtrahend = root.sum - root.left.sum
    else:
        # root.key == end
        if root.right is not None:
            # Get sum of key that are bigger than end range, need to subtract it from total sum (excluding root key)
            right_subtrahend = root.right.sum

    # Update total sum (remove numbers after range end)
    total_sum = total_sum - right_subtrahend

    return total_sum


# ------------------------------------------------------------------------------------------- #
# Debugging tool to print different tree orders and placement (e.g. where print_tree is being called from)

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

        # Traverse to left child, then right child, then parent
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


# ------------------------------------------------------------------------------------------- #
# Input and tree variable initialization


root = None
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
