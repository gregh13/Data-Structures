import sys


def solve(k, text, pattern):
	results = []

	len_t = len(text)
	len_p = len(pattern)

	mismatches = 0
	match_found = False

	for i in range(len_t - len_p):
		for j in range(len_p):
			char_t = text[i:(j+1)]
			if pattern[j] != char_t:
				mismatches += 1
				if mismatches > k:
					match_found = False
					break
		if match_found:
			results.append(i)
			mismatches = 0
			match_found = False

	return results


for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
