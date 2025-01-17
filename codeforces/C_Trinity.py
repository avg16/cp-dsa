def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort() #o(n logn)
    ops = 0
    #now two pointers
    l,r = 0,2
    ans = n-2
    while r<n:
        while r-l>=2 and arr[l]+arr[l+1]<=arr[r]:
            l+=1
        ans = min(ans,n-(r-l+1))
        r+=1
    return print(ans)

res = []
for _ in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)