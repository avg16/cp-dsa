t = int(input())
while t > 0:
    n = int(input())
    print("1", end=" ")
    for i in range(2, n-1):
        print(i-1, end=" ")
    print("1 2")
    t -= 1