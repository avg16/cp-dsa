t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

# def mode(arr):
#     freq = {}
#     for num in arr:
#         freq[num] = freq.get(num, 0) + 1
#     return max(freq, key=freq.get)
# def solve(arr):
#     n = len(arr)
#     b = []
#     for i in range(n):
#         b.append(arr[i])
#         curr_mode = mode(b)
#         if curr_mode != arr[i]:
#             new_b = list(reversed(b))
#             for j in range(0,len(new_b)//2 + 1):
#                 if new_b[j] != arr[i]:
#                     new_b[j] = arr[i]
#                     break
#     return new_b

def solve(arr):
    s= set()
    for i in range(n):
        s.add(i + 1)
    result = []
    for i in range(n):
        if arr[i] in s:
            result.append(arr[i])
            s.remove(arr[i])
        else:
            result.append(min(s))
            s.remove(min(s))

    return result

results = []
for n, arr in test_cases:
    results.append(solve(arr))

for res in results:
    print(*res)