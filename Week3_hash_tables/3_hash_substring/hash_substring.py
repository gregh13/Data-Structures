import random


def hash_function(string, multiplier, prime):
    # Polynomial hash function - loops through each char in string, converts to int, updates hash val
    ans = 0
    for c in reversed(string):
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def hashing_solution(pattern, text):
    # Store common operations as variables for convenience
    text_len = len(text)
    pattern_len = len(pattern)
    t_minus_p = text_len - pattern_len

    # Initialize hash array and empty match list
    hashes = [None] * (t_minus_p + 1)
    match_positions = []

    # Choosing an appropriately large prime number is essential to keeping hash collisions low
    # However, too large a prime for a simple input will cause the arithmetic to be slower
    prime_list = [2_207, 3_010_349, 1_000_000_007, 1_000_000_000_193,
                  2_305_843_009_213_693_951, 618_970_019_642_690_137_449_562_111]

    # Initialize prime number to smallest in list, set counter to next index
    prime = prime_list[0]
    counter = 1

    while 5 * text_len * pattern_len > prime and counter < len(prime_list):
        prime = prime_list[counter]
        counter += 1

    multiplier = random.randint(1, prime - 1)

    pattern_hash = hash_function(pattern, multiplier, prime)
    hashes[t_minus_p] = hash_function(text[t_minus_p:], multiplier, prime)

    y = 1
    for _ in range(pattern_len):
        y = (y * multiplier) % prime

    for i in range((t_minus_p-1), -1, -1):
        hashes[i] = ((multiplier * hashes[i+1]) + ord(text[i]) - (y * ord(text[i + pattern_len]))) % prime

    for j in range(t_minus_p+1):
        if hashes[j] != pattern_hash:
            continue
        if pattern == text[j:(j+pattern_len)]:
            match_positions.append(j)

    return match_positions


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
    # print_occurrences(get_occurrences_naive(*read_input()))
    print_occurrences(hashing_solution(*read_input()))

