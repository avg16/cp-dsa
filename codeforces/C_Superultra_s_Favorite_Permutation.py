# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# for _ in range(int(input())):
#     n = int(input())
#     arr = [x for x in range(n)]
#     ans = []
#     for i in range(n):
#         for j in range(i,n):
#             if is_prime(arr[i] + arr[j])==True:
#                 continue
#             else:
#                 ans.append()

def prefix_sum(arr):
    n = len(arr)
    for i in range(1, n):
        arr[i] += arr[i - 1]
    return arr

for _ in range(int(input())):
    n = int(input())
    arr = [x for x in range(n)]
    ps = prefix_sum(arr)
    for i in range(n):
        if i > 0:
            print(ps[i] - ps[i - 1], end=' ')
        else:
            print(ps[i], end=' ')
    print()

