for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    def f1(a):
        op=1
        for i in range(0,len(a),2):
            op=max(op,a[i+1]-a[i])   
        return op
        
    if n%2==0:
        print(f1(arr))
    else:
        op=10**18
        for i in range(n):
            op=min(op,f1(arr[:i]+arr[i+1:]))
        print(op)