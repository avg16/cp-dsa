t= int(input())
test_cases = []
for _ in range(t):
    n,m,k = map(int,input().split())
    list_arr = list(map(int,input().split()))
    k_arr = list(map(int,input().split()))
    test_cases.append((n,m,k,list_arr,k_arr))

def solve(n,m,k,list_arr,k_arr):
    ans = [0]*(len(list_arr))
    copy = list_arr
    for i in range(len(k_arr)):
        if k_arr[i] in list_arr:
            list_arr.remove(k_arr[i])
    for i in range(len(list_arr)):
        for j in range(len(copy)):
            if list_arr[i] == copy[j]:
                ans[j] += 1
    return "".join(map(str, ans))

res= []
for n,m,k,list_arr,k_arr in test_cases:
    res.append(solve(n,m,k,list_arr,k_arr))
for i in res:
    print(i)
