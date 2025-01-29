for _ in range(int(input())):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    s = sum(arr)
    m = max(arr)
    print(max(m, (s+x-1)//x))