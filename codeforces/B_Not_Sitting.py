# def distance(a,b,c,d):
#     return abs(a-c) + abs(b-d)
# def solve():
#     n,m = map(int,input().split())
#     all_max_dist = []
#     for i in range(0,n):
#         for j in range(0,m):
#             d1 = i+j
#             d2 = i + (m-j-1)
#             d3 = (n-i-1) + j
#             d4 = (n-i-1) + (m-j-1)
#             all_max_dist.append(max(d1,d2,d3,d4))
#     all_max_dist.sort()
#     for i in range(0,n*m):
#         print(all_max_dist[i],end=" ")
# res = []
# for i in range(int(input())):
#     res.append(solve())
# for i in res:
#     if i!= None:
#         print(i)

def distance(a, b, c, d):
    return abs(a - c) + abs(b - d)

def solve():
    n, m = map(int, input().split())
    all_max_dist = []
    for i in range(0, n):
        for j in range(0, m):
            d1 = i + j
            d2 = i + (m - j - 1)
            d3 = (n - i - 1) + j
            d4 = (n - i - 1) + (m - j - 1)
            all_max_dist.append(max(d1, d2, d3, d4))
    all_max_dist.sort()
    return ' '.join(str(x) for x in all_max_dist)

cases = int(input())
for _ in range(cases):
    print(solve())