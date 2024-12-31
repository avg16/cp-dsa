# t= int(input())
# test_cases = []
# for i in range(t):
#     a= input()
#     b = input()
#     c= input()
#     test_cases.append((a,b,c))

# def count_changes(a, b, c):
#     i, j = 0, 0
#     count = 0

#     for char in c:
#         if i < len(a) and char == a[i]:
#             i += 1
#         elif j < len(b) and char == b[j]:
#             j += 1
#         else:
#             count += 1

#     return count
# results = []
# for a, b, c in test_cases:
#     results.append(count_changes(a, b, c))

# for res in results:
#     print(res)

import sys
from math import inf

a = input().strip()
b = input().strip()
res = input().strip()
def solve(a,b,res):
    n, m = len(a), len(b)
    # Initialize DP table with infinity
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    # Fill first row and column
    for i in range(n):
        dp[i + 1][0] = dp[i][0] + (a[i] != res[i])
    for j in range(m):
        dp[0][j + 1] = dp[0][j] + (b[j] != res[j])
    
    # Fill the rest of the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(
                dp[i - 1][j] + (a[i - 1] != res[i + j - 1]),
                dp[i][j - 1] + (b[j - 1] != res[i + j - 1])
            )

    print(dp[n][m])

def main():
    tests = int(input().strip())
    for _ in range(tests):
        solve()

if __name__ == "__main__":
    main()
