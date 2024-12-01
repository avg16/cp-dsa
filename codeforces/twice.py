def maximum_score(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        freq = {}
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        score = sum(f // 2 for f in freq.values())
        results.append(score)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = maximum_score(t, test_cases)
for res in results:
    print(res)

    