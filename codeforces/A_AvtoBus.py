def solve():
    n = int(input())
    if n % 2 == 1 or n < 4:
        return print(-1)
    else:
        mn = n // 6
        if n % 6 != 0:
            mn += 1
        mx = n // 4
        return print(mn, mx)

res = []
for i in range(int(input())):
    res.append(solve())

for i in range(len(res)):
    if res[i]!=None:
        print(res[i])