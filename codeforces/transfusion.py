# def possibility(arr):
#     n =len(arr)
#     mean = sum(arr)/n
#     for j in range(1,n-2):
#         while arr[j] != mean:
#             if arr[j-1]<arr[j]:
#                 arr[j-1]+=1
#                 arr[j+1]-=1
#             elif arr[j-1]>arr[j]:
#                 arr[j-1]-=1
#                 arr[j+1]+=1
#             else:
#                 break
#     return arr,"YES" if arr==[mean]*n else "NO"
def possibility(arr):
    odd_sum = 0
    even_sum =0
    for i in range(len(arr)):
        if arr[i]%2==0:
            even_sum+=arr[i]
        else:
            odd_sum+=arr[i]
    odd_places = n//2
    even_places = n-odd_places
    if (odd_sum%odd_places==0 and even_sum%even_places==0 and odd_sum/odd_places==even_sum/even_places):
        print('YES')
    else:
        print('NO')

t=int(input())
test_cases = []
for _ in range(t):
    n= int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n,arr))

results = []
for n,arr in test_cases:
    results.append(possibility(arr))
for res in results:
    print(res)