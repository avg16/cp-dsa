# t= int(input())
# test_cases = []
# for _ in range(t):
#     n,m,k = map(int,input().split())
#     list_arr = list(map(int,input().split()))
#     k_arr = list(map(int,input().split()))
#     test_cases.append((n,m,k,list_arr,k_arr))

# def solve(n,m,k,list_arr,k_arr):
#     ans = [0]*(len(list_arr))
#     copy = list_arr
#     for i in range(len(k_arr)):
#         if k_arr[i] in list_arr:
#             list_arr.remove(k_arr[i])
#     for i in range(len(list_arr)):
#         for j in range(len(copy)):
#             if list_arr[i] == copy[j]:
#                 ans[j] += 1
#     return "".join(map(str, ans))

# res= []
# for n,m,k,list_arr,k_arr in test_cases:
#     res.append(solve(n,m,k,list_arr,k_arr))
# for i in res:
#     print(i)
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))
    used = [False for i in range(n + 1)]
    for i in q:
        used[i] = True
    l = len(q)
    for i in range(m):
        if l == n or (l == n-1 and not used[a[i]]):
            print(1, end='')
        else:
            print(0, end='')
    print()