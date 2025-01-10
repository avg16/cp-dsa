def penalty(arr):
    score = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            score += 1
    return score

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    score = 0
    i = 1
    while i < n:
        if a[i] < a[i-1]:
            a.pop(i-1)
            score += penalty(a)
        else:
            i += 1
    return score

res = []
for _ in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)
