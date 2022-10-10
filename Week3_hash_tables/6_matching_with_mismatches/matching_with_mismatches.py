import sys


def solve(k, text, pattern):
	len_t = len(text)
	len_p = len(pattern)

	for i in range(len_t - len_p):
		for char in text:

	return []


for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
