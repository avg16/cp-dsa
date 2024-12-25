t= int(input())
test_cases = []
for _ in range(t):
    n,k = map(int,input().split())
    n_arr = list(map(int,input().split()))
    test_cases.append((n,k,n_arr))

def solve(n,k,n_arr):
    copy = n_arr
    # will traverse through array, for each element, difference from every other element will be observed
    for i in range(len(n_arr)):
        for j in range(len(copy)):
            diff = abs(n_arr[i]-n_arr[j])
            if diff ==0:
                continue
            elif diff%k==0:
                