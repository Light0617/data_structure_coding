# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if parent[table] != table:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source, ans):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return [False, ans]

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        ans = lines[realDestination] if lines[realDestination] > ans else ans

    elif rank[realDestination] == rank[realSource]:
        rank[realDestination] += 1

        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        ans = lines[realDestination] if lines[realDestination] > ans else ans

    else:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
        ans = lines[realSource] if lines[realSource] > ans else ans

    return [True, ans]
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    _, ans = merge(destination - 1, source - 1, ans)
    print(ans)
    
