def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ops = 0
    less_than2 =0
    for i in range(1,len(a)-1):
        if a[i]<2:
            less_than2 += 1
    if (less_than2 == len(a) - 2) or (len(a)==3 and a[1]%2 ==1):
        return print(-1)
    for i in range(1,len(a)-1):
        ops += (a[i] + 1)//2
    return print(ops)
results = []
for i in range(int(input())):
    results.append(solve())
for i in results:
    if i != None:
        print(i)