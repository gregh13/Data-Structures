# python3

import sys


class Rope:
	def __init__(self, s):
		self.s = s

	def result(self):
		return self.s

	def process(self, i, j, k):
		# Use slicing to quickly cut and paste parts of a string
		left_part = self.s[:i]
		cut_part = self.s[i:j+1]
		right_part = self.s[j+1:]
		small_join = left_part + right_part
		# k is the index number of the smaller join list where cut part needs to be inserted
		new_left = small_join[:k]
		new_right = small_join[k:]
		self.s = new_left + cut_part + new_right
		return


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
