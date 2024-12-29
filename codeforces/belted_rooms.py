t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input()
    test_cases.append((n, s))

def solve(n, s):
    hasCW = False
    hasCCW = False 
    for c in s:
        if c == '>':
            hasCW = True
        if c == '<':
            hasCCW = True
    if hasCW and hasCCW:
        s+=s[0]
        ans =0
        for i in range(n):
            if s[i] == '-' or s[i+1] == '-':
                ans += 1
        return ans
    else:
        return n

results = []
for n, s in test_cases:
    results.append(solve(n, s))

for res in results:
    print(res)