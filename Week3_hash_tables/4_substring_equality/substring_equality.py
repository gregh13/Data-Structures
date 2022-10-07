import sys
import random


class HashSolution:
	def __init__(self, string):
		self.string = string
		self.string_len = len(string)

		self.hash_table_1 = [0] * self.string_len
		self.hash_table_2 = [0] * self.string_len

		self.power = 10 ** 9
		self.mod_1 = self.power + 7
		self.mod_2 = self.power + 9
		self.x = random.randint(1, self.power - 1)

		self.a_index = -1
		self.b_index = -1
		self.sub_len = -1

		self.precompute_hashes()

	def query_input(self, a_i, b_i, length):
		self.a_index = a_i
		self.b_index = b_i
		self.sub_len = length

	def calc_substring_hash(self, hash_table, prime):
		a_hash = hash_table[self.a_index + self.sub_len] - ((self.x * self.sub_len) * hash_table[self.a_index]) % prime
		b_hash = hash_table[self.b_index + self.sub_len] - ((self.x * self.sub_len) * hash_table[self.b_index]) % prime
		return a_hash, b_hash

	def precompute_hashes(self):
		for i in range(1, self.string_len):
			self.hash_table_1[i] = (self.x * self.hash_table_1[i-1] + ord(self.string[i])) % self.mod_1
			self.hash_table_2[i] = (self.x * self.hash_table_2[i-1] + ord(self.string[i])) % self.mod_2

	def check_substrings(self):









class SolverNaive:
	def __init__(self, s):
		self.s = s

	def ask(self, a, b, l):
		return s[a:a+l] == s[b:b+l]


s = sys.stdin.readline()
q = int(sys.stdin.readline())
# solver = SolverNaive(s)
# for _ in range(q):
# 	a, b, l = map(int, sys.stdin.readline().split())
# 	print("Yes" if solver.ask(a, b, l) else "No")

hashbrowns = HashSolution(s)
for _ in range(q):
	hashbrowns.query_input(map(int, sys.stdin.readline().split()))
	hashbrowns.check_substrings()

