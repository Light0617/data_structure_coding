# python3

import sys, threading
import collections
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def build_tree(self):
                graph = {}
                root = -1
                for i, num in enumerate(self.parent):
                        if num == -1:
                                root = i
                        else:
                                child, mother = i, num
                                if mother not in graph:
                                        graph[mother] = []
                                graph[mother].append(child)
                return [graph, root]

        def compute_height(self):
                return self.compute_height_bfs()

        ## BFS to do level travesal        
        def compute_height_bfs(self):
                graph, root = self.build_tree()
                q = collections.deque([root])
                depth = 0
                while q:
                        size = len(q)
                        for _ in range(size):
                                node = q.popleft()
                                if node not in graph:
                                        continue
                                for child in graph[node]:
                                        q.append(child)
                        depth += 1

                return depth

        #DFS with recursive
        def compute_height_recursive(self):
                def helper(graph, node):
                        if node not in graph or graph[node] == 0:
                                return 1
                        else:
                                return max([helper(graph, kid) for kid in graph[node]]) + 1

                graph, root = self.build_tree()
                return helper(graph, root)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
