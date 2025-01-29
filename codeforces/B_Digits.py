import math
 
for _ in range(int(input())):
    n, d = map(int, input().split())
    n = min(n, 7)
    s = d * (10**math.factorial(n) - 1) // 9
    for i in (1, 3, 5, 7, 9):
        if s % i == 0:
            print(i, end=' ')
    print()