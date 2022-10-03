from collections import deque


def deque_solution(sequence, m):
    max_values = []
    de = deque([])
    # Initialize deque with first window elements (excluding last element of window)
    de.extend(sequence[:m-1])

    for i in range(len(sequence) - m + 1):
        for _ in range(len(de)):
            if de[-1] <= sequence[i]:
                de.pop()
        de.append(sequence[i])
        max_values.append(max(de))





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

