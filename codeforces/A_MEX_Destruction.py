def mex(arr):
    s = set(arr)
    i = 0
    while True:
        if i not in s:
            return i
        i += 1


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    while a and a[-1] == 0:
        a.pop()

    a = a[::-1]
    while a and a[-1] == 0:
        a.pop()
    a = a[::-1]

    if not a:
        print(0)
        return

    hasZero = any(x == 0 for x in a)
    if hasZero:
        return print(2)
    else:
        return print(1)

results = []
for i in range(int(input())):
    results.append(solve())
for i in results:
    if i != None:
        print(i)