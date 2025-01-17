for _ in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    s+="D"
    a=[[int(i) for i in input().split()] for _ in range(n)]
    i=0
    j=0
    for c in s:
        if c=="D":
            a[i][j]=-sum(a[i])
            i+=1
        else:
            a[i][j]=-sum(a[k][j] for k in range(n))
            j+=1
    for l in a:
        print(*l)
