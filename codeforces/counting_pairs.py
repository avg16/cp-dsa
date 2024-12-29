# t = int(input())
# test_cases = []
# for _ in range(t):
#     n,x,y = map(int,input().split())
#     arr = list(map(int,input().split()))
#     test_cases.append((n,x,y,arr))

# def solve(n,x,y,arr):
#     ans = 0
#     pairs =[]
#     # if you simultaneously remove the elements at positions 𝑖 and 𝑗 from the sequence , the sum of the remaining elements is at least 𝑥 and at most y
#     for i in range(n):
#         for j in range(i+1,n):
#             if sum(arr[:i]) + sum(arr[j:]) >= x and sum(arr[:i]) + sum(arr[j:]) <= y:
#                 ans += 1
#     return ans
# results = []
# for n,x,y,arr in test_cases:
#     results.append(solve(n,x,y,arr))

# for res in results:
#     print(res)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n, x, y = map(int, data[idx:idx + 3])
        idx += 3
        arr = list(map(int, data[idx:idx + n]))
        idx += n
 
        total_sum = sum(arr)
 
        arr.sort()
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                remaining_sum = total_sum - arr[i] - arr[j]
                if x <= remaining_sum <= y:
                    count += 1
        
        results.append(count)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")
solve()