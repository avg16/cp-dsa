from collections import defaultdict

N = int(2e5 + 5)

def dfs3(u, adj2, col, visited2, component_count):
    col[u] = component_count
    visited2[u] = True
    for v in adj2[u]:
        if not visited2[v]:
            dfs3(v, adj2, col, visited2, component_count)

def dfs(u, adj1, visited, mp):
    visited[u] = True
    for v in adj1[u]:
        if not visited[v] and (u, v) not in mp:
            dfs(v, adj1, visited, mp)

def solve():
    t = int(input())
    for _ in range(t):
        n, m1, m2 = map(int, input().split())
        
        adj1 = defaultdict(list)
        adj2 = defaultdict(list) 
        visited1 = [False] * n
        visited2 = [False] * n
        col = [0] * n
        mp = {}
        
        for _ in range(m1):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            adj1[u].append(v)
            adj1[v].append(u)
        
        for _ in range(m2):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            adj2[u].append(v)
            adj2[v].append(u)
        
        component_count = 0
        for i in range(n):
            if not visited2[i]:
                component_count += 1
                dfs3(i, adj2, col, visited2, component_count)
        ans = 0
        for i in range(n):
            for v in adj1[i]:
                if col[i] != col[v]:
                    ans += 1
                    mp[(i, v)] = 1
                    mp[(v, i)] = 1
        
        cnt2 = 0
        for i in range(n):
            if not visited1[i]:
                cnt2 += 1
                dfs(i, adj1, visited1, mp)
        
        print(ans // 2 + (cnt2 - component_count))

if __name__ == "__main__":
    solve()

