def solve(): 
    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a)
    while n>1:
        n =n-1
        a = [a[i+1]-a[i] for i in range(n)]
        ans =max(ans, abs(sum(a)))
    print(ans)
res =[]
for i in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)