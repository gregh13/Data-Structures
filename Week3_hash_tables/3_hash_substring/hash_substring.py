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

    # Makes sure prime number is sufficiently large for the given input sizes
    while 5 * text_len * pattern_len > prime and counter < len(prime_list):
        prime = prime_list[counter]
        counter += 1

    # Randomize hash multiplier based on final prime value
    multiplier = random.randint(1, prime - 1)

    # Calculate the input pattern hash
    pattern_hash = hash_function(pattern, multiplier, prime)

    # Calculate last substring hash, used to calculate rest of text hashes
    hashes[t_minus_p] = hash_function(text[t_minus_p:], multiplier, prime)

    # Initialize coefficient value to 1, then calc for pattern
    y = 1
    for _ in range(pattern_len):
        y = (y * multiplier) % prime

    # Calculate all remaining possible hashes for the text in reverse order, using rabin-karp trick
    # This loop computes all hash values of length pattern in the text to use for quick comparison with pattern hash
    for i in range((t_minus_p-1), -1, -1):
        hashes[i] = ((multiplier * hashes[i+1]) + ord(text[i]) - (y * ord(text[i + pattern_len]))) % prime

    # Compare precomputed text hashes with pattern hash.
    for j in range(t_minus_p+1):

        # If hashes don't match, substrings don't match
        if hashes[j] != pattern_hash:
            continue

        # If hashes match, need to check for collision cases (i.e. make sure strings are actually equal)
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

