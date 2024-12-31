for _ in range(int(input())):
    n = int(input())
    ans =1
    cur =1
    while True:
        if cur>=n:
            print(ans)
            break
        ans+=1
        cur = cur*2 + 2 #after4th index, then 10th index, then further, to maximise.