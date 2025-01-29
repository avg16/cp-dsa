def solve():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    k = r - l + 1

    prefix = sorted(a[:r])[:k]
    prefix_sum = sum(prefix)

    suffix = sorted(a[l-1:])[:k]
    suffix_sum = sum(suffix)

    print(min(prefix_sum, suffix_sum))

t = int(input())
for _ in range(t):
    solve()
