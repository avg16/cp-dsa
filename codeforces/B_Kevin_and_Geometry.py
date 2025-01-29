for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    l2=[]
    a.sort()
    eq=-1
    for i in range(n-1, 0, -1):
        if a[i]==a[i-1]:
            eq=a[i]
            l2=a[:i-1]+a[i+1:]
            break
    for i in range(len(l2)-1):
        if l2[i+1]-l2[i]<eq*2:
            print(eq, eq, l2[i], l2[i+1])
            break
    else:
        print(-1)