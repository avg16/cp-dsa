for _ in range(int(input())):
    n = int(input())
    if n%2==0:
        for i in range(n//2):
            print(i+1, i+1)
    else:
        if n<=25:
            print(-1)
        else:
            print("1 3 3 4 4 5 5 6 6 1 2 7 7 8 8 9 9 10 10 11 11 12 12 13 13 1 2")
            for i in range(14, n//2+1):
                print(i, ' ', i)

