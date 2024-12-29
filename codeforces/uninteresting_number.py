t= int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    test_cases.append(n)

def solve(n):
    s2  = 2
    s3 = 3
    if n%9==0:
        return print("YES")
    dig_sum = sum([int(i) for i in str(n)])
    if (dig_sum+2)%9==0:
        if s2 in [int(i) for i in str(n)]:
            i = 4
            return print("YES")
    elif (dig_sum + 6)%9 ==0:
        if s3 in [int(i) for i in str(n)]:
            i = 9
            return print("YES")
    elif (dig_sum + 8)%9 ==0:
        if s3 in [int(i) for i in str(n)]:
            i = 9
        if s2 in [int(i) for i in str(n)]:
            i = 4
        return print("YES")
    else:
        return print("NO")

for n in test_cases:
    solve(n)