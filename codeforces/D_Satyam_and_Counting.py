from collections import Counter

for _ in range(int(input())):
    n = int(input())
    nums = [tuple(map(int, input().split())) for _ in range(n)]
    check = set(nums)
    b = Counter(x for x, y in nums)
    ans = sum(n-2 for x in b if b[x]==2)
    ans += sum(1 for x, y in check if (x-1,y^1) in check and (x+1, y^1) in check)
    print(ans)