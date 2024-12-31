def solve():
    n = int(input())
    return ' '.join(str(2*i - 1) for i in range(1,n+1))

res = []
for _ in range(int(input())):
    res.append(solve())
for i in res:
    print(i)