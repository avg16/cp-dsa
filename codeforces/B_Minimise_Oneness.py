def solve():
    n = int(input())
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(0)
        else:
            l.append(1)
    return print(''.join(map(str, l)))
 
res = []
for i in range(int(input())):
    res.append(solve())
for i in range(len(res)):
    if res[i]!= None:
        print(res[i])