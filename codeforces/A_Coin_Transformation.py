def solve():
    n = int(input())
    div =1
    while n>3:
        n = n//4
        div*=2
    return print(div)
res =[]
for _ in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)