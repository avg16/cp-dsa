import math
def find_dimensions(t, test_cases):
    results = []
    for k, arr in test_cases:
        target = k - 2
        possible_dimensions = set()

        for i in range(1, int(math.sqrt(target)) + 1):
            if target % i == 0:
                possible_dimensions.add(i)
                possible_dimensions.add(target // i)
        found = False
        for n in possible_dimensions:
            m = target // n
            if n in arr and m in arr:
                results.append((n, m))
                found = True
                break
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((k, arr))

results = find_dimensions(t, test_cases)
for n, m in results:
    print(n, m)
