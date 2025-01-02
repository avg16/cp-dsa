def solve():
    n, s, m = map(int, input().split())
    segs = [[0, 0], [m, m]] + [list(map(int, input().split())) for i in range(n)]
    segs.sort()
    for i in range(1, n + 2):
        if segs[i][0] - segs[i - 1][1] >= s:
            print('YES')
            return
    print('NO')

res = []
for _ in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)