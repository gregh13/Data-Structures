from collections import deque


def deque_solution(sequence, m):
    max_values = []
    # Get initial values for first window (minus right-most element)
    initial_values = [(sequence[i], i) for i in range(m-1)]
    # Initialize deque
    de = deque([initial_values])

    for i in range(m-1, len(sequence)):
        for _ in range(len(de)):
            if de[-1][0] <= sequence[i]:
                de.pop()
        de.append((sequence[i], i))
        max_values.append(max(de))
        if de[0][1] == i:
            de.popleft()

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

    print(*max_sliding_window_naive(input_sequence, window_size))
    print("-----------")
    print(*deque_solution(input_sequence, window_size))
