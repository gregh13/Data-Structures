# python3

import sys


class Rope:
	def __init__(self, s):
		self.s = s

	def result(self):
		return self.s

	def process_naive(self, i, j, k):
		left_part = self.s[:i]
		cut_part = self.s[i:j]
		right_part = self.s[j:]
		small_join = left_part + right_part
		new_left = small_join[:k]
		new_right = small_join[k:]
		self.s = new_left + cut_part + new_right
		pass


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process_naive(i, j, k)
print(rope.result())
