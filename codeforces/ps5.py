import numpy as np
import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    test_case_op = []
    for i in range(t):
        q = int(input())
        n = int(input())
        edges = []
        curr = set()
        for _ in range(n):
            A, B, rate, commission = input().split()
            curr.add(A)
            curr.add(B)
            r_eff = float(rate) * (1 - float(commission) / 100)
            weight = -np.log(r_eff)
            edges.append((A, B, weight))
        que = []
        for _ in range(q):
            src, tgt = input().split()
            que.append((src, tgt))

        currency_list = list(curr)
        num_curr = len(currency_list)
        c_to_i = {c: i for i, c in enumerate(currency_list)}

        edge_list = []
        for A, B, weight in edges:
            u = c_to_i[A]
            v = c_to_i[B]
            edge_list.append((u, v, weight))

        curr_op = []
        for src, tgt in que:
            if src not in c_to_i or tgt not in c_to_i:
                curr_op.append("-1")
                continue
            src_idx = c_to_i[src]
            tgt_idx = c_to_i[tgt]
            V = num_curr
            INF = float('inf')
            dis = [INF] * V
            dis[src_idx] = 0
            for i in range(V - 1):
                updated = False
                for u, v, w in edge_list:
                    if dis[u] != INF and dis[u] + w < dis[v]:
                        dis[v] = dis[u] + w
                        updated = True
                if not updated:
                    break

            if dis[tgt_idx] == INF:
                curr_op.append("-1")
            else:
                effective_rate = np.exp(-dis[tgt_idx])
                f_rate = "{0:.6f}".format(effective_rate)
                f_rate = f_rate.rstrip('0').rstrip('.') if '.' in f_rate else f_rate
                curr_op.append(f_rate)

        test_case_op.append(curr_op)

    for i, op in enumerate(test_case_op):
        print('\n'.join(op))
        if i < len(test_case_op) - 1:
            print()

solve()