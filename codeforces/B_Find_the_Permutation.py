import sys
input = sys.stdin.readline
print = sys.stdout.write

def cmp(u, v):
    if u < v:
        return g[u][v] == '1'
    return g[v][u] == '0'

def solve():
    n = int(input())
    global g
    g = []
    for _ in range(n):
        g.append(input().strip())

    p = list(range(n))
    
    from functools import cmp_to_key
    p.sort(key=cmp_to_key(lambda x, y: -1 if cmp(x, y) else 1))

    result = [str(x + 1) for x in p]
    print(' '.join(result) + '\n')

t = int(input())
while t > 0:
    solve()
    t -= 1