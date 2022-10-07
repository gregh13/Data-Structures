import sys
import random


class HashSolution:
	def __init__(self, string):
		self.string = string
		self.s_len = len(string)
		self.hash_table_1 = [0] * self.s_len
		self.hash_table_2 = [0] * self.s_len
		self.power = 10 ** 9
		self.mod_1 = self.power + 7
		self.mod_2 = self.power + 9
		self.x = random.randint(1, self.power - 1)

	def query_input(self, a, b, length):
		self.a = a
		self.b = b
		self.l = length

	def hash_func(self, substring, x, prime):
		hash = 0
		for char in reversed(substring):
			hash = (hash * x + ord(char)) % prime
		return hash

	def precompute_hashes(self, mod1, mod2):
		for i in range(1, self.s_len):
			self.hash_table_1[i] = (self.x * self.hash_table_1[i-1] + ord(self.string[i])) % mod1
			self.hash_table_2[i] = (self.x * self.hash_table_2[i-1] + ord(self.string[i])) % mod2






class SolverNaive:
	def __init__(self, s):
		self.s = s

	def ask(self, a, b, l):
		return s[a:a+l] == s[b:b+l]


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = SolverNaive(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
