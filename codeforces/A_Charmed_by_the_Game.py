for _ in range(int(input())):
    a, b= map(int, input().split())
    total_games = a + b
    ans = set()
    mx = max(a,b)
    mi= min(a,b)
    for i in range(0, 2*mi+1, 2):
        ans.add(i+(mx-mi)//2 )
        ans.add(i+(mx-mi+1)//2)
    ans = list(ans)
    ans.sort()
    print(len(ans))
    print(*ans)