# t = int(input())
# test_cases = []
# for _ in range(t):
#     n,m,d = map(int,input().split())
#     p_arr = list(map(int,input().split()))
#     m_arr = list(map(int,input().split()))
#     test_cases.append((n,m,d,p_arr,m_arr))

# def pos(x, p_arr):
#     for i in range(len(p_arr)):
#         if p_arr[i] == x:
#             return i+1

# def solve(n, m, d, p_arr, m_arr):
#     min_swaps = float('inf')
#     for i in range(m-1):
#         if pos(m_arr[i], p_arr) >= pos(m_arr[i+1], p_arr):
#             min_swaps = 0
#             break
#         elif pos(m_arr[i+1], p_arr) - pos(m_arr[i], p_arr) > d:
#             min_swaps = 0
#             break
#         else n - pos(m_arr[i+1], p_arr) + pos(m_arr[i], p_arr) - 1 >= d + 1 - (pos(m_arr[i+1], p_arr) - pos(m_arr[i], p_arr)):
#             min_swaps = min(min_swaps, pos(m_arr[i+1], p_arr) - pos(m_arr[i], p_arr))
#     return min_swaps

# results = []
# for n,m,d,p_arr,m_arr in test_cases:
#     results.append(solve(n,m,d,p_arr,m_arr))
# for res in results:
#     print(res)

from sys import stdin

sz = 10**5 + 10
p = [0] * sz
a = [0] * (sz + 1)
pos = [0] * sz

def main():
    t = int(stdin.readline().strip())
    while t > 0:
        n, m, d = map(int, stdin.readline().strip().split())
        for i in range(1, n+1):
            p[i] = int(stdin.readline().strip())
            pos[p[i]] = i
        for i in range(1, m+1):
            a[i] = int(stdin.readline().strip())
        ans = 10**9
        for i in range(m-1):
            if pos[a[i+1]] <= pos[a[i]] or pos[a[i+1]] - pos[a[i]] > d:
                ans = 0
                break
            ans = min(ans, pos[a[i+1]] - pos[a[i]])
            dist = pos[a[i+1]] - pos[a[i]]
            swapNeed = d - dist + 1
            swapPossible = (pos[a[i]] - 1) + (n - pos[a[i+1]])
            if swapPossible >= swapNeed:
                ans = min(ans, swapNeed)
        print(ans)
        t -= 1

if __name__ == "__main__":
    main()