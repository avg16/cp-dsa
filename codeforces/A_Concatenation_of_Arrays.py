for _ in range(int(input())):
    arr = []
    for i in range(int(input())):
       [x,y] = map(int, input().split())
       arr.append([x+y,x,y])
    arr.sort()
    print(" ".join(f"{e[1]} {e[2]}" for e in arr))