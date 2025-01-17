def solve():
    n,k = map(int,input().split())
    if n==1:
        return print('1\n1')
    if k==1 or k==n:
        return print(-1)
    p2,p3 = k- k%2 , k+1 + k%2
    print(f'3\n1 {p2} {p3}')

res =[]
for _ in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)