def solve():
    n = int(input())
    a = [0]
    for x in input().split():
        x = int(x)
        a.append(a[-1] + x)
    s = input()
    ans = 0
    l = 0
    r = n - 1
    while r > l:
        while l < n and s[l] == 'R':
            l += 1
        while r >= 0 and s[r] == 'L':
            r -= 1
        if l < r:
            ans += a[r + 1] - a[l]
            l += 1
            r -= 1
    print(ans)
 
t = int(input())
for _ in range(t):
    solve()