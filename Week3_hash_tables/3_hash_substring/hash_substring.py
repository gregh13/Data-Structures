

def hash_function(string, multiplier, prime):
    ans = 0
    for c in reversed(string):
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def hashing_solution(pattern, text):
    text_len = len(text)
    pattern_len = len(pattern)
    t_minus_p = text_len - pattern_len

    hashes = [] * t_minus_p
    match_positions = []

    prime_list = [3_010_349, 1_000_000_007, 1_000_000_000_193,
                  2_305_843_009_213_693_951, 618_970_019_642_690_137_449_562_111]
    prime = prime_list[0]
    multiplier = 263

    counter = 1
    while text_len * pattern_len > prime and counter < len(prime_list):
        prime = prime_list[counter]
        counter += 1

    pattern_hash = hash_function(pattern, multiplier, prime)
    hashes[(t_minus_p - 1)] = hash_function(text[t_minus_p:], multiplier, prime)

    y = 0
    for _ in range(pattern_len):
        y = (y * multiplier) % prime

    for i in range((t_minus_p-2), -1, -1):
        hashes[i] = ((multiplier * hashes[i+1]) + text[i] - (y * text[i + pattern_len])) % prime

    for j in range(t_minus_p):
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
    print_occurrences(get_occurrences_naive(*read_input()))

