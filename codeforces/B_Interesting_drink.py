def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())

    a.sort()

    for _ in range(m):
        k = int(input())
        ans = len([x for x in a if x <= k])
        print(ans)

solve()