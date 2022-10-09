import sys
import random


class HashSolution:
	def __init__(self, string):
		self.string = string
		self.string_len = len(string) + 1

		self.hash_table_1 = [0] * self.string_len
		self.hash_table_2 = [0] * self.string_len

		self.coef_table_1 = [1] * self.string_len
		self.coef_table_2 = [1] * self.string_len

		self.power = 10 ** 9
		self.mod_1 = self.power + 7
		self.mod_2 = self.power + 9
		self.x = random.randint(1, self.power - 1)

		self.a_index = -1
		self.b_index = -1
		self.sub_len = -1

		self.precompute_hashes_coefs()

	def precompute_hashes_coefs(self):
		for i in range(1, self.string_len):
			self.hash_table_1[i] = (self.x * self.hash_table_1[i-1] + ord(self.string[i-1])) % self.mod_1
			self.hash_table_2[i] = (self.x * self.hash_table_2[i-1] + ord(self.string[i-1])) % self.mod_2

			self.coef_table_1[i] = (self.coef_table_1[i-1] * self.x) % self.mod_1
			self.coef_table_2[i] = (self.coef_table_2[i-1] * self.x) % self.mod_2

	def query_input(self, a_i, b_i, length):
		self.a_index = a_i
		self.b_index = b_i
		self.sub_len = length

	def calc_substring_hash(self, hash_table, prime, coef_table):
		a_hash = hash_table[self.a_index + self.sub_len] - (coef_table[self.sub_len] * hash_table[self.a_index])
		b_hash = hash_table[self.b_index + self.sub_len] - (coef_table[self.sub_len] * hash_table[self.b_index])

		a_hash = (a_hash + prime) % prime
		b_hash = (b_hash + prime) % prime
		return a_hash == b_hash

	def check_substrings(self):
		if self.calc_substring_hash(self.hash_table_1, self.mod_1, self.coef_table_1):
			if self.calc_substring_hash(self.hash_table_2, self.mod_2, self.coef_table_2):
				print("Yes")
			else:
				print("No")
		else:
			print("No")










class SolverNaive:
	def __init__(self, s):
		self.s = s

	def ask(self, a, b, l):
		return s[a:a+l] == s[b:b+l]


s = sys.stdin.readline()
q = int(sys.stdin.readline())

hashbrowns = HashSolution(s)
for _ in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	hashbrowns.query_input(a, b, l)
	hashbrowns.check_substrings()

# naive_solver = SolverNaive(s)
# for _ in range(q):
# 	a, b, l = map(int, sys.stdin.readline().split())
# 	print("Yes" if naive_solver.ask(a, b, l) else "No")

