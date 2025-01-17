# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(2):
        a.append(list(map(int, input().split())))
    best = [max(a[0][i], a[1][i]) for i in range(n)]
    full = [a[0][i] + a[1][i] for i in range(n)]
    sum_best = sum(best)
    ans = -10 ** 19
    for i in range(n):
        ans = max(ans, sum_best + full[i] - best[i])
    print(ans)