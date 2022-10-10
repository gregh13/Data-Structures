import sys


def naive_solution(k, text, pattern):
	results = []

	len_t = len(text)
	len_p = len(pattern)

	mismatches = 0
	no_match = False

	for i in range((len_t+1) - len_p):
		for j in range(len_p):
			char_t = text[i+j:i+j+1]
			if pattern[j] != char_t:
				mismatches += 1
				if mismatches > k:
					no_match = True
					break
		if not no_match:
			results.append(i)

		no_match = False
		mismatches = 0

	return results


for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = naive_solution(int(k), t, p)
	print(len(ans), *ans)
