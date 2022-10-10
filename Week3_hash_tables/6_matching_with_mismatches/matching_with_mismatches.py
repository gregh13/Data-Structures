import sys
import random


class HashMismatch:
	def __init__(self, k, text, pattern):
		self.k = k
		self.text = text
		self.pattern = pattern
		self.results = []
		self.mismatches = 0

		self.len_t = len(text) + 1
		self.len_p = len(pattern)
		self.t_min_p = self.len_t - self.len_p

		self.power = 10**9
		self.mod_a = self.power + 1957
		self.mod_b = self.power + 2233
		self.x = random.randint(1, self.power)

		self.hashes_1a = [0] * self.len_t
		self.hashes_1b = [0] * self.len_t
		self.coefs_1a = [1] * self.len_t
		self.coefs_1b = [1] * self.len_t

		self.hashes_2a = [0] * (self.len_p + 1)
		self.hashes_2b = [0] * (self.len_p + 1)
		self.coefs_2a = [1] * (self.len_p + 1)
		self.coefs_2b = [1] * (self.len_p + 1)

		self.precompute_values()

	def precompute_values(self):
		for i in range(1, self.len_t):
			self.hashes_1a = (self.x * self.hashes_1a[i-1] + ord(self.text[i-1])) % self.mod_a
			self.hashes_1b = (self.x * self.hashes_1b[i-1] + ord(self.text[i-1])) % self.mod_b

			self.coefs_1a = (self.coefs_1a[i-1] * self.x) % self.mod_a
			self.coefs_1b = (self.coefs_1b[i-1] * self.x) % self.mod_b

		for i in range(1, (self.len_p + 1)):
			self.hashes_2a = (self.x * self.hashes_2a[i-1] + ord(self.pattern[i-1])) % self.mod_a
			self.hashes_2b = (self.x * self.hashes_2b[i-1] + ord(self.pattern[i-1])) % self.mod_b

			self.coefs_2a = (self.coefs_2a[i-1] * self.x) % self.mod_a
			self.coefs_2b = (self.coefs_2b[i-1] * self.x) % self.mod_b

	def binary_mismatch_search(self, left, right, mismatches):
		mid = (left + right) // 2

		hash_t = self.hashes_1a[mid] - (self.coefs_1a[left] * self.hashes_1a[left])
		hash_t = (hash_t + self.mod_a) % self.mod_a

		hash_p = self.hashes_2a[mid] - (self.coefs_2a[left] * self.hashes_2a[left])
		hash_p = (hash_p + self.mod_a) % self.mod_a

		if hash_t != hash_p:
			right = mid - 1
			self.binary_mismatch_search(left, right, mismatches)



	def find_mismatches(self):
		# Loop through all position in text that fit pattern size
		for i in range(self.t_min_p):
			# Use binary search to find mismatches
			self.binary_mismatch_search(i, i + self.len_p, 0)















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
