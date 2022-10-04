# python3


def build_heap(data, n):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """

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

    def sift_down(parent_index, size):

        min_index = parent_index

        child_1_index = 2*parent_index + 1
        child_2_index = 2*parent_index + 2

        if child_1_index <= size and data[child_1_index] < data[min_index]:
            min_index = child_1_index

        if child_2_index <= size and data[child_2_index] < data[min_index]:
            min_index = child_2_index

        if parent_index != min_index:
            data[min_index], data[parent_index] = data[parent_index], data[min_index]
            sift_down(min_index, size)
        return

    swaps = []
    size = n - 1

    for i in range(size//2, 0, -1):
        sift_down(i, size)

    return swaps


def selection_sort_naive(data):
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def check_answer(data, n):
    size = n - 1

    for i in range(size):
        child_1 = 2*i + 1
        child_2 = 2*i + 2
        if data[i] > data[child_1] or data[i] > data[child_2]:
            print("INCORRECT!")
            print("Index of parent, child_1, child_2: ", i, child_1, child_2)
            print("Value at parent, child_1, child_2: ", data[i], data[child_1], data[child_2])
            break

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    # print("Data Raw: ", data)
    # swaps_naive = selection_sort_naive(data)
    swaps = build_heap(data, n)

    print(len(swaps))
    # for i, j in swaps[]:
    #     print(i, j)
    # print("Data Sorted: ", data[n-50:])

    # print(len(swaps_naive))
    # for i, j in swaps_naive:
    #     print(i, j)
    check_answer(data, n)

if __name__ == "__main__":
    main()
