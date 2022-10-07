import sys


class HashSolution:
	def __init__(self, string):
		self.string = string

	def hash_func(self, substring, x, prime):
		hash = 0
		for char in reversed(substring):
			hash = (hash * x + ord(char)) % prime
		return hash




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
