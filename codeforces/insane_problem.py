import numpy as np
t = int(input())
test_cases=[]
for i in range(t):
    k,l_1,r_1,l_2,r_2 = map(int,input().split())
    test_cases.append((k,l_1,r_1,l_2,r_2))

#brute force
# def solve1(k,l_1,r_1,l_2,r_2):
#     ordered_pair_count = 0
#     for i in range(l_1,r_1+1):
#         for j in range(l_2,r_2+1):
#             ratio = j/i
#             if np.log(ratio)/np.log(k) == int(np.log(ratio)/np.log(k)):
#                 ordered_pair_count += 1
#                 print((i,j))
#             elif np.log(ratio) ==0:
#                 ordered_pair_count += 1
#                 print((i,j))
#     return ordered_pair_count

def solve2(k,l_1,r_1,l_2,r_2):
    u=1
    ans = 0
    while (u<=1e9):
        ans += max(min(r_2//u,r_1)-max((l_2+u-1)//u,l_1)+1,0)
        u*=k
    return ans

results = []
for k,l_1,r_1,l_2,r_2 in test_cases:
    results.append(solve2(k,l_1,r_1,l_2,r_2))

for res in results:
    print(res)