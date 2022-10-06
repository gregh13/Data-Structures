

def hash_function(string):
    _multiplier = 263
    _prime = 1000000007
    ans = 0
    for c in reversed(string):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans % buckets


def hashing_solution(pattern, text):
    text_len = len(text)
    pattern_len = len(pattern)
    t_minus_p = text_len - pattern_len

    hashes = [None] * t_minus_p
    hashes[(t_minus_p - 1)] = 0





    pass




def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences_naive(*read_input()))

