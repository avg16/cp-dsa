def solve():
    n = int(input())
    a = list(map(int, input().split()))
    unique_color = 0
    more_than_1 = 0
    d = {}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    for key, value in d.items():
        if value == 1:
            unique_color += 1
        elif value>1:
            more_than_1 += 1
    return more_than_1 + 2*((unique_color+1)//2)

results = []
for _ in range(int(input())):
    results.append(solve())
for res in results:
    print(res)