def solve():
    t = int(input())
    for _ in range(t):
        arr = [0] * 5
        arr[0], arr[1], arr[3], arr[4] = map(int, input().split())
        
        ans = 0
        arr[2] = arr[3] - arr[1] 
        for i in range(2, 5):
            if arr[i] == arr[i - 1] + arr[i - 2]:
                ans += 1
        
        res = 0
        arr[2] = arr[0] + arr[1]
        for i in range(2, 5):
            if arr[i] == arr[i - 1] + arr[i - 2]:
                res += 1
        
        print(max(res, ans)) 

if __name__ == '__main__':
    solve()


        