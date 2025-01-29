import sys
def solve():
    input = sys.stdin.readline
    t= int(input())
    for _ in range(t):
        n = int(input())
        currencies = set()
        edges = []
        for _ in range(n):
            A,B,w = input().split()
            currencies.add(A)
            currencies.add(B)
            edges.append((A,B,float(w)))
        
        currency_list = list(currencies)
        num_curr= len(currency_list)
        if num_curr == 0:
            print("NO")
            continue
        
        c_to_i = {c:i for i,c in enumerate(currency_list)}
        dummynode = num_curr
        V = num_curr+1

        all_edges = []
        for A, B, w in edges:
            u = c_to_i[A]
            v = c_to_i[B]
            all_edges.append((u,v,w))
            all_edges.append((v,u,-w))

        for i in range(num_curr):
            all_edges.append((dummynode, i, 0))
        
        INF = float('inf')
        dis = [INF]*V
        dis[dummynode] = 0
        
        for i in range(V-1):
            updated = False
            for u, v, w in all_edges:
                if dis[u] != INF and dis[u] + w < dis[v]:
                    dis[v] = dis[u] + w
                    updated = True
            if not updated:
                break

        cycle = False
        for u, v, w in all_edges:
            if dis[u] != INF and dis[u]+w<dis[v]:
                cycle = True
                break
        
        print("YES" if cycle else "NO")

solve()