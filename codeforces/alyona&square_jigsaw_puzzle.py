t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

def solve(arr):
    sqs = set()
    k = 1
    while k * k <= 100 * 1000:
        sqs.add(k * k)
        k += 2
    ans =0
    block_sum = 0
    for i in range(n):
        block_sum += arr[i]
        if block_sum in sqs:
            ans += 1
    return ans

results = []
for n, arr in test_cases:
    results.append(solve(arr))

for res in results:
    print(res)