from collections import defaultdict
for _ in range(int(input())):
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = defaultdict(int)
    for i in range(n-1):
        cur = (i+1)*(n-i-1)
        m[cur] += a[i+1] - a[i] - 1
        m[cur+i] += 1
    m[n-1] += 1
    a = [m[i] for i in b]
    print(*a)
