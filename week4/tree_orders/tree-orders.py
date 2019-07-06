# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def find_root(self):
    visited = [False] * len(self.key)
    for left, right in zip(self.left, self.right):
      visited[left] = True
      visited[right] = True

    for v in visited:
      if not v:
        return v
    return 0

  def inOrder(self):
    def helper(node):
      if self.left[node] != -1:
        helper(self.left[node])
      self.result.append(self.key[node])
      if self.right[node] != -1:
        helper(self.right[node])

    self.result = []
    root = self.find_root()
    helper(root)  
    return self.result

  def preOrder(self):
    def helper(node):
      self.result.append(self.key[node])
      if self.left[node] != -1:
        helper(self.left[node])
      if self.right[node] != -1:
        helper(self.right[node])

    self.result = []
    root = self.find_root()
    helper(root)  
    return self.result

  def postOrder(self):
    def helper(node):
      if self.left[node] != -1:
        helper(self.left[node])
      if self.right[node] != -1:
        helper(self.right[node])
      self.result.append(self.key[node])

    self.result = []
    root = self.find_root()
    helper(root)  
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
