import sys
import random


class HashMismatch:
	def __init__(self, k, text, pattern):
		self.k = int(k)
		self.text = text
		self.pattern = pattern
		self.results = []

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
			self.hashes_1a[i] = (self.x * self.hashes_1a[i-1] + ord(self.text[i-1])) % self.mod_a
			self.hashes_1b[i] = (self.x * self.hashes_1b[i-1] + ord(self.text[i-1])) % self.mod_b

			self.coefs_1a[i] = (self.coefs_1a[i-1] * self.x) % self.mod_a
			self.coefs_1b[i] = (self.coefs_1b[i-1] * self.x) % self.mod_b

		for i in range(1, (self.len_p + 1)):
			self.hashes_2a[i] = (self.x * self.hashes_2a[i-1] + ord(self.pattern[i-1])) % self.mod_a
			self.hashes_2b[i] = (self.x * self.hashes_2b[i-1] + ord(self.pattern[i-1])) % self.mod_b

			self.coefs_2a[i] = (self.coefs_2a[i-1] * self.x) % self.mod_a
			self.coefs_2b[i] = (self.coefs_2b[i-1] * self.x) % self.mod_b

	def binary_mismatch_search(self, left, right, text_index):
		if left >= right:
			index = left
			return index

		mid = (left + right) // 2
		mid_2 = mid - text_index
		left_2 = left - text_index

		hash_1a = self.hashes_1a[mid] - (self.coefs_1a[left] * self.hashes_1a[left])
		hash_2a = self.hashes_2a[mid_2] - (self.coefs_2a[left_2] * self.hashes_2a[left_2])

		hash_1a = (hash_1a + self.mod_a) % self.mod_a
		hash_2a = (hash_2a + self.mod_a) % self.mod_a

		if hash_1a != hash_2a:
			right = mid
			index = self.binary_mismatch_search(left, right, text_index)
		else:
			hash_1b = self.hashes_1b[mid] - (self.coefs_1b[left] * self.hashes_1b[left])
			hash_2b = self.hashes_2b[mid_2] - (self.coefs_2b[left_2] * self.hashes_2b[left_2])

			hash_1b = (hash_1b + self.mod_b) % self.mod_b
			hash_2b = (hash_2b + self.mod_b) % self.mod_b

			if hash_1b != hash_2b:
				right = mid
				index = self.binary_mismatch_search(left, right, text_index)
			else:
				left = mid + 1
				index = self.binary_mismatch_search(left, right, text_index)

		return index

	def find_mismatches(self):
		# Loop through all position in text that fit pattern size
		for i in range(self.t_min_p):

			mismatches = 0
			left = i
			right = i + self.len_p

			# Check to see if pattern contains 1 more than max allowed mismatches
			for _ in range(self.k + 1):
				# Use binary search to find mismatches
				result_index = self.binary_mismatch_search(left, right, i)

				if result_index == i + self.len_p:
					# No more mismatches
					break
				else:
					mismatches += 1
					left = result_index + 1

			# Add result if under threshold
			if mismatches <= self.k:
				self.results.append(i)

	def print_results(self):
		print(len(self.results), *self.results)
		return







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
	hashbrowns = HashMismatch(k, t, p)
	hashbrowns.find_mismatches()
	hashbrowns.print_results()
	# ans = naive_solution(int(k), t, p)
	# print(len(ans), *ans)
