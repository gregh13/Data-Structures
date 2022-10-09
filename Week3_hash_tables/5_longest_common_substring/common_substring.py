# python3

import sys
from collections import namedtuple
import random

Answer = namedtuple('answer_type', 'i j len')


def hashing_algorithm(str_1, str_2):
	def precompute_hashes_coefs():
		h_table_1a[0] = ord(str_1) % mod_1
		h_table_1b[0] = ord(str_1) % mod_2

		h_table_2a[0] = ord(str_2) % mod_1
		h_table_2b[0] = ord(str_2) % mod_2

		for i in range(1, len_1):
			h_table_1a[i] = (x * h_table_1a[i - 1] + ord(str_1[i - 1])) % mod_1
			coef_table_1a[i] = (coef_table_1a[i - 1] * x) % mod_1
			h_table_1b[i] = (x * h_table_1b[i - 1] + ord(str_1[i - 1])) % mod_2
			coef_table_1b[i] = (coef_table_1b[i - 1] * x) % mod_2

		for i in range(1, len_2):
			h_table_2a[i] = (x * h_table_2a[i - 1] + ord(str_2[i - 1])) % mod_1
			coef_table_2a[i] = (coef_table_2a[i - 1] * x) % mod_1
			h_table_2b[i] = (x * h_table_2b[i - 1] + ord(str_2[i - 1])) % mod_2
			coef_table_2b[i] = (coef_table_2b[i - 1] * x) % mod_2

	def binary_hash_search():
		not_found = True
		k = max_len // 2

		while not_found:
			for
				a_hash = hash_table[j + k] - (coef_table[k] * hash_table[a_index])
				a_hash = (a_hash + prime) % prime

		return a_hash

	len_1 = len(str_1)
	len_2 = len(str_2)

	h_table_1a = [0] * (len_1)
	h_table_1b = [0] * (len_1)

	h_table_2a = [0] * (len_2)
	h_table_2b = [0] * (len_2)

	coef_table_1a = [1] * (len_1)
	coef_table_1b = [1] * (len_1)

	coef_table_2a = [1] * (len_2)
	coef_table_2b = [1] * (len_2)

	power = 10 ** 9
	mod_1 = power + 87
	mod_2 = power + 223
	x = random.randint(1, power)

	max_len = 0

	if len_1 < len_2:
		max_len = len_1
	else:
		max_len = len_2

	precompute_hashes_coefs()












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
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
