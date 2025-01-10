import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    brand_cost = [0] * k
    for _ in range(k):
        b, c = map(int, sys.stdin.readline().split())
        brand_cost[b - 1] += c
    brand_cost.sort(reverse=True)
    ans = sum(brand_cost[:min(n, k)])
    print(ans)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()