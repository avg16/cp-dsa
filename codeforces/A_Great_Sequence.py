def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    arr.sort()
    ans = 0

    for i in range(n):
        if d[arr[i]] == 0:
            continue
        if arr[i] * x in d and d[arr[i] * x] > 0:
            d[arr[i]] -= 1
            d[arr[i] * x] -= 1
        else:
            ans += 1
            d[arr[i]] -= 1
    return ans
res = []
for _ in range(int(input())):
    res.append(solve())
for i in res:
    print(i)