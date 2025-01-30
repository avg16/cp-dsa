def solve():
    n, q = map(int, input().split())

    pre1 = [[0]*26 for _ in range(n+1)]
    pre2 = [[0]*26 for _ in range(n+1)]

    s1 = input()
    s2 = input()

    for i in range(1, n+1):
        pre1[i][ord(s1[i-1])-ord('a')]+= 1
        pre2[i][ord(s2[i-1])-ord('a')]+= 1

        for j in range(26):
            pre1[i][j] += pre1[i - 1][j]
            pre2[i][j] += pre2[i - 1][j]

    for _ in range(q):
        l, r = map(int, input().split())
        dif = 0

        for c in range(26):
            v1 = pre1[r][c] - pre1[l - 1][c]
            v2 = pre2[r][c] - pre2[l - 1][c]

            dif += abs(v1 - v2)

        print(dif // 2)

tc = int(input())
for _ in range(tc):
    solve()