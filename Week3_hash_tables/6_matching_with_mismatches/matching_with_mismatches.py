import sys
import random


class HashMismatch:
	def __init__(self, k, text, pattern):
		self.k = k
		self.text = text
		self.pattern = pattern

		self.len_t = len(text) + 1
		self.len_p = pattern
		self.t_min_p = self.len_t - self.len_p

		self.power = 10**9
		self.mod_1 = self.power + 1957
		self.mod_2 = self.power + 2233
		self.x = random.randint(1, self.power)

		self.hashes = [0] * self.len_t
		self.coefs = [1] * self.len_t

	def precompute_values(self):
		for i in range(self.len_t):











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
