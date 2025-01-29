def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
 
    ans = 0
    j = 0
    for i in range(n):
        j = max(j, i)
        while j + 1 < n and a[j + 1] <= a[j] + 1 and a[j + 1] < a[i] + k:
            j += 1
        ans = max(ans, j - i + 1)
    print(ans)
 
t = int(input())
for _ in range(t):
    solve()