def calc(n):
    if n<3:
        return 1
    return 1 + calc(n/3)
pr =[0]*(300000)
pr[1] = 1
for i in range(2,300000):
    pr[i] = pr[i-1] + calc(i)
def solve():
    l,r = map(int,input().split())
    ans = calc(l)*2 + pr[r] - pr[l]
    return print(ans)
res = []
for _ in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)