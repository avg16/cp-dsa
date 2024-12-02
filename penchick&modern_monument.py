def min_ops(arr):
    ops = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            ops += 1
    return ops

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

results = []
for n, arr in test_cases:
    results.append(min_ops(arr))

for res in results:
    print(res)
