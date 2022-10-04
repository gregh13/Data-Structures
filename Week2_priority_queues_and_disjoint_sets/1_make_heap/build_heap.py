# python3


def build_heap(data, n):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    def sift_up(child_index):
        if child_index == 0:
            return
        parent_index = (child_index - 1) // 2
        # Sort ascending, so check if child is less than parent.
        if data[child_index] < data[parent_index]:
            # If so, need to swap values
            data[child_index], data[parent_index] = data[parent_index], data[child_index]

            # Add swap to swap list:
            swaps.append((child_index, parent_index))

            # Continue sifting up using child's new index (i.e. parent_index)
            sift_up(parent_index)

        # Child and parent value are in order, no swaps needed
        return

    def sift_down(index):
        pass

    swaps = []

    for i in range(n):



    return swaps


def selection_sort_naive(data):
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps_naive = selection_sort_naive(data, n)
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    print(len(swaps_naive))
    for i, j in swaps_naive:
        print(i, j)


if __name__ == "__main__":
    main()
