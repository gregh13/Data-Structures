# python3

import sys
from collections import namedtuple
import random

Answer = namedtuple('answer_type', 'i j len')


def hashing_algorithm(str_1, str_2):
	def precompute_hashes_coefs():
		# Calculate hashes and coefficients for first string with both hash functions (i.e. both prime modulos)
		for i in range(1, len_1):
			h_table_1a[i] = (x * h_table_1a[i - 1] + ord(str_1[i - 1])) % mod_a
			coef_table_1a[i] = (coef_table_1a[i - 1] * x) % mod_a
			h_table_1b[i] = (x * h_table_1b[i - 1] + ord(str_1[i - 1])) % mod_b
			coef_table_1b[i] = (coef_table_1b[i - 1] * x) % mod_b

		# Same for second string
		for i in range(1, len_2):
			h_table_2a[i] = (x * h_table_2a[i - 1] + ord(str_2[i - 1])) % mod_a
			coef_table_2a[i] = (coef_table_2a[i - 1] * x) % mod_a
			h_table_2b[i] = (x * h_table_2b[i - 1] + ord(str_2[i - 1])) % mod_b
			coef_table_2b[i] = (coef_table_2b[i - 1] * x) % mod_b

	def binary_hash_search():
		# Initialize result, while loop condition check, left & right bounds, and calculate k (the midpoint)
		result = Answer(0, 0, 0)
		not_found = True
		left = 1
		right = max_len
		k = (left + right) // 2

		# Use binary search to find optimal value of k (i.e. the length of longest common substring)
		while not_found:
			# Initialize substring dictionary and loop flag
			sub_h_dict_1a = {}
			match_found = False

			# Loop through all possible substrings of length k in first string, storing values in dictionary
			for index_1 in range(len_1 - k):
				# Calculate substring hashes for first string
				hash_1a = h_table_1a[index_1 + k] - (coef_table_1a[k] * h_table_1a[index_1])
				# Process to safeguard against negative number modulo errors
				hash_1a = (hash_1a + mod_a) % mod_a
				# Store hash in dictionary as the key, with its as the value
				sub_h_dict_1a[hash_1a] = index_1

			# Loop through all possible substrings of length k in second string, checking with first string dict
			for index_2 in range(len_2 - k):
				# Calculate substring hashes for second string
				hash_2a = h_table_2a[index_2 + k] - (coef_table_2a[k] * h_table_2a[index_2])
				# Negative number modulo safeguard
				hash_2a = (hash_2a + mod_a) % mod_a
				# Search for match in sub hash dict
				if hash_2a in sub_h_dict_1a:
					# Now check with second hash function to make sure it isn't a hashing collision
					hash_1b = h_table_1b[sub_h_dict_1a[hash_2a] + k] - (coef_table_1b[k] * h_table_1b[sub_h_dict_1a[hash_2a]])
					hash_2b = h_table_2b[index_2 + k] - (coef_table_2b[k] * h_table_2b[index_2])
					# Negative number safeguard
					hash_1b = (hash_1b + mod_b) % mod_b
					hash_2b = (hash_2b + mod_b) % mod_b

					if hash_2b == hash_1b:
						# Match found, update answer
						result = Answer(sub_h_dict_1a[hash_2a], index_2, k)
						# Check if binary search is complete
						if k == left:
							# Change while loop check
							not_found = False
							match_found = True
							break
						# Update left bound, search for larger size of k (i.e. check if longer substring exists)
						left = k
						match_found = True
						break

			if not match_found:
				# Update right bound, search for smaller size of k (i.e. check if a smaller substring exists)
				right = k
				# Check if binary search is complete
				if k == left:
					not_found = False
					break

			# Update k for next iteration since left or right bound has changed above
			k = (left + right) // 2

		return result

	# Initialize string lengths with one added for better looping and indexing operations
	len_1 = len(str_1) + 1
	len_2 = len(str_2) + 1

	# Initialize two hash tables for each string (use two hash functions to avoid collisions)
	h_table_1a = [0] * (len_1)
	h_table_1b = [0] * (len_1)

	h_table_2a = [0] * (len_2)
	h_table_2b = [0] * (len_2)

	# Initialize two hash tables for each string
	coef_table_1a = [1] * (len_1)
	coef_table_1b = [1] * (len_1)

	coef_table_2a = [1] * (len_2)
	coef_table_2b = [1] * (len_2)

	# Initialize two prime modulos used for hashing and multiplier x
	power = 10 ** 9
	mod_a = power + 87
	mod_b = power + 223
	x = random.randint(1, power)

	# Initialize and calculate max common string length to check (will be bounded by smaller string length)
	max_len = 0
	if len_1 < len_2:
		max_len = len_1
	else:
		max_len = len_2

	# Use precomputation and binary search to get answer
	precompute_hashes_coefs()
	answer = binary_hash_search()

	return answer








def solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans


for line in sys.stdin.readlines():
	s, t = line.split()
	# ans = solve(s, t)
	# print("------------------")
	# print(ans.i, ans.j, ans.len)
	# print("---")
	hash_answer = hashing_algorithm(s, t)
	print(hash_answer.i, hash_answer.j, hash_answer.len)
