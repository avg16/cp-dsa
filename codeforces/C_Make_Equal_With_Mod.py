def solve():
    n = int(input())
    a =list(map(int, input().split()))
    # a --> a mod x 
    a.sort()
    one = False
    consec = False
    for i in range(n):
        if a[i]== 1:
            one = True
        if i<n-1 and a[i] +1 == a[i+1]:
            consec = True
    if one and consec:
        return print("NO")
    else:
        return print("YES")

for i in range(int(input())):
    solve()