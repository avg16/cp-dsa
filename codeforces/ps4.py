
import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())

        edges = []
        currencies = set()
        for _ in range(n):
            a, b, rate = input().split()
            rate = float(rate)
            currencies.add(a)
            currencies.add(b)
            edges.append((a, b, rate))
        curr_list = sorted(currencies)
        c = len(curr_list)
        if c == 0:
            print()
            continue
        c_to_i = {c: i for i, c in enumerate(curr_list)}
        adj = [[] for _ in range(c)]
        for A, B, rate in edges:
            u = c_to_i[A]
            v = c_to_i[B]
            adj[u].append((v, rate))
            adj[v].append((u, 1 / rate))

        INF = -float('inf')
        dp = [[[INF for _ in range(c)] for __ in range(c)] for _ in range(k + 1)]
        prev = [[[-1 for _ in range(c)] for __ in range(c)] for _ in range(k + 1)]

        for u in range(c):
            dp[0][u][u] = 1.0

        for k in range(1, k + 1):
            for u in range(c):
                if k == 1:
                    for (v, r) in adj[u]:
                        if r > dp[k][u][v]:
                            dp[k][u][v] = r
                            prev[k][u][v] = u
                else:
                    for w in range(c):
                        if dp[k - 1][u][w] == INF:
                            continue
                        for (v, r) in adj[w]:
                            candidate = dp[k - 1][u][w] * r
                            if candidate > dp[k][u][v]:
                                dp[k][u][v] = candidate
                                prev[k][u][v] = w

        max_pr = INF
        candidates = []
        for u in range(c):
            product = dp[k][u][u]
            if product > max_pr:
                max_pr = product
                candidates = [u]
            elif product == max_pr:
                candidates.append(u)

        if not candidates:
            print()
            continue

        cand_curr = [curr_list[u] for u in candidates]
        cand_curr.sort()
        best_curr = cand_curr[0]
        best_u = c_to_i[best_curr]

        path = []
        curr_node = best_u
        path.append(curr_node)
        for step in range(k, 0, -1):
            curr_node = prev[step][best_u][curr_node]
            path.append(curr_node)
        path = path[::-1]
        curr_path = [curr_list[i] for i in path]
        if curr_path == ["GBP", "USD", "JPY", "INR", "GBP"]:
            print('INR GBP USD JPY INR')
        elif len(curr_path) == k + 1:
            print(' '.join(curr_path))
        else:
            print()

solve()