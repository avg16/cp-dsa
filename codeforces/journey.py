t = int(input())
test_cases = []
for _ in range(t):
    n,a,b,c = map(int,input().split())
    test_cases.append((n,a,b,c))

#brute force
# def journey(n,a,b,c):
#     total_journey = 0
#     day_count=0
#     while total_journey<n:
#         total_journey+=a
#         day_count+=1
#         if total_journey<n:
#             total_journey+=b
#             day_count+=1
#         if total_journey<n:
#             total_journey+=c
#             day_count+=1
#     return day_count

def journey(n,a,b,c):
    minimum_d = (int(n/(a+b+c)))*3
    n%=(a+b+c)
    if n>0:
        n-=a
        minimum_d+=1
    if n>0:
        n-=b
        minimum_d+=1
    if n>0:
        n-=c
        minimum_d+=1
    return minimum_d


results = []
for n,a,b,c in test_cases:
    results.append(journey(n,a,b,c))

for res in results:
    print(res)
