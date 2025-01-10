# def prefix_sum(arr):
#     for i in range(1, len(arr)):
#         arr[i] += arr[i-1]
#     return arr

# def solve():
#     n = int(input())
#     binary_s = input()
#     arr = [int(i) for i in binary_s]
#     max_c = max(prefix_sum(arr))

#     for i in range(n):
#         if prefix_sum(arr[0:i+1])[-1] == max_c/2:
#             return print(i+1)
#         else:
#             return print(0)


# res = []
# for _ in range(int(input())):
#     res.append(solve())
# for i in res:
#     if i != None:
#         print(i)

for case in range(int(input())):
    n = int(input())
    a = input()
    suf_cnt = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf_cnt[i] = suf_cnt[i + 1] + (a[i] == '1')
    pref_cnt = 0
     
    opt_ans = -1
    opt_dist = n * 2
    threshold = (n + 1) // 2
     
    for i in range(n + 1):
        if pref_cnt >= (i + 1) // 2 and suf_cnt[i] >= (n - i + 1) // 2 and abs(n - 2 * i) < opt_dist:
            opt_dist = abs(n - 2 * i)
            opt_ans = i
        if i != n:
            pref_cnt += (a[i] == '0')
     
    print(opt_ans)