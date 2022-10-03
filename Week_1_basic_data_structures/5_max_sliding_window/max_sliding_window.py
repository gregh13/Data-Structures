from collections import deque


def deque_solution(sequence, m):
    # Initialize list
    max_values = []

    # Get initial values for first window (minus right-most element)
    initial_values = [(sequence[i], i) for i in range(m-1)]

    # Sort initial values
    initial_values.sort(reverse=True)

    # Initialize deque
    de = deque(initial_values)

    # Loop through all windows, with i starting at the index value of the window's right bound
    for i in range(m-1, len(sequence)):
        for _ in range(len(de)):
            # Reduces size of deque by removing smaller items (i.e. less than window right bound)
            if de[-1][0] <= sequence[i]:
                de.pop()
            else:
                # Since values are already sorted descending, can stop checking
                break
        # Add window's right bound item
        de.append((sequence[i], i))

        # Since values are sorted, max value in window will be the first value in the deque
        max_values.append(de[0][0])

        # Prepare for next window, remove all values in deque that are out of window left bound
        # Since values are sorted by max_val and not by index, while loop helps remove any old values
        while de[0][1] <= i-(m-1):
            # Remove item that's index is less than the next windows left bound
            de.popleft()

            # Prevent index error by exiting when deque is empty
            if not de:
                break

    return max_values


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    # print(*max_sliding_window_naive(input_sequence, window_size))
    # print("-----------")
    print(*deque_solution(input_sequence, window_size))
