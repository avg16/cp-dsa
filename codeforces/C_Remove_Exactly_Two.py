
# from heapq import heappush, heappop
# from collections import defaultdict

# def solve():
#     n = int(input())
#     adj = defaultdict(list)
    
#     for _ in range(n-1):
#         u, v = map(int, input().split())
#         adj[u].append(v)
#         adj[v].append(u)
    
#     pq = []
#     for v in range(1, n+1):
#         heappush(pq, (-len(adj[v]), v))
    
#     while pq:
#         deg, v = heappop(pq)
#         deg = -deg
#         if deg == len(adj[v]):
#             first_components = deg
#             removed_vertex = v
#             break
    
#     remaining_adj = defaultdict(list)
#     for v in adj:
#         if v != removed_vertex:
#             remaining_adj[v] = [u for u in adj[v] if u != removed_vertex]
    
#     pq = []
#     for v in remaining_adj:
#         heappush(pq, (-len(remaining_adj[v]), v))
    
#     second_components = 0
#     while pq:
#         deg, v = heappop(pq)
#         deg = -deg
#         if deg == len(remaining_adj[v]):
#             second_components = deg
#             break
    
#     return first_components + second_components - 1

# t = int(input())
# for _ in range(t):
#     print(solve())

# def main():
#     t = int(input())
#     while t > 0:
#         n = int(input())

#         adj = [[] for _ in range(n + 1)]
#         deg = [0] * (n + 1)

#         for _ in range(n - 1):
#             u, v = map(int, input().split())
#             adj[u].append(v)
#             adj[v].append(u)
#             deg[u] += 1
#             deg[v] += 1

#         if n == 2:
#             print(0)
#         else:
#             sorted_vertices = sorted(
#                 [(deg[i], i) for i in range(1, n + 1)], reverse=True)

#             K = min(200, n)

#             top_k_vertices = [v for _, v in sorted_vertices[:K]]
#             top_k_set = set(top_k_vertices)

#             adj_top_k = {v: set() for v in top_k_vertices}
#             for v in top_k_vertices:
#                 for neighbor in adj[v]:
#                     if neighbor in top_k_set:
#                         adj_top_k[v].add(neighbor)

#             best_pair = 0
#             for i in range(K):
#                 for j in range(i + 1, K):
#                     v1 = top_k_vertices[i]
#                     v2 = top_k_vertices[j]

#                     deg_sum = deg[v1] + deg[v2]

#                     if v2 in adj_top_k[v1]:
#                         deg_sum -= 1

#                     best_pair = max(best_pair, deg_sum)

#             print(best_pair - 1)

#         t -= 1

# if __name__ == "__main__":
#     main()

def solve():
    n = int(input())
    arr = [[] for _ in range(n + 1)]
    adj = [set() for _ in range(n + 1)]
    d = [0] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)
        adj[u].add(v)
        adj[v].add(u)
        d[u] += 1
        d[v] += 1

    if n == 2:
        print(0)
        return

    k = 500
    node_top = sorted([(d[i], i) for i in range(1, n + 1)], reverse=True)
    vec = [node[1] for node in node_top[:min(k, n)]]

    ans = 0
    for i in range(len(vec)):
        for j in range(i + 1, len(vec)):
            u = vec[i]
            v = vec[j]

            temp = d[u] + d[v]
            if v not in adj[u]:
                temp -= 1
                ans = max(ans, temp)
                continue
            temp -= 2

            ans = max(ans, temp)

    ans = min(ans, n - 2)
    print(ans)

t = int(input())
for _ in range(t):
    solve()