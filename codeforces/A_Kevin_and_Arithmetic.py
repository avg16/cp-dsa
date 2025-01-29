for _ in range(int(input())):
    n=int(input())
    arr=[int(i)%2 for i in input().split()]
    arr.sort()
    print((1-arr[0])+sum(arr[1:]))