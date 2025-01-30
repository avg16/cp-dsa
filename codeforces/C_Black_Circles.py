# def distance(x1, y1, x2, y2):
#     return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# def solve():
#     n = int(input())
#     coord = []
#     for _ in range(n):
#         x, y = map(int, input().split())
#         coord.append((x, y))
#     xs, ys, xt, yt = map(int, input().split())
#     p2p_dis = distance(xs, ys, xt, yt)
#     c2p_dis = [distance(x, y, xt, yt) for x, y in coord]
#     b= True
#     for i in c2p_dis:
#         if i <= p2p_dis:
#             b= False
#             break
#     print("YES" if b else "NO")

# t = int(input())
# for _ in range(t):
#     solve()
# import sys

def dis(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2
import sys
def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        x = [0]*(n+1)
        y = [0]*(n+1)

        for i in range(1,n+1):
            x[i],y[i]=map(int,input().split())

        xs,ys,xt,yt = map(int, input().split())
        ok=True
        for i in range(1,n+1):
            if dis(xt,yt,x[i],y[i])<=dis(xt,yt,xs,ys):
                ok = False
                break

        print("YES" if ok else "NO")
solve()