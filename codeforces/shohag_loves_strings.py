##########TLE############
# def count_distinct_substrings(s):
#     substrings = set()
#     n = len(s)
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             substrings.add(s[i:j])
#     return len(substrings)

# def find_valid_p(s):
#     n = len(s)
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             p = s[i:j]
#             if count_distinct_substrings(p) % 2 == 0:
#                 return p
#     return -1

# def solve(test_cases):
#     results = []
#     for s in test_cases:
#         results.append(find_valid_p(s))
#     return results

# t = int(input())
# test_cases = [input().strip() for _ in range(t)]
# answers = solve(test_cases)
# print(answers)


for __ in range(int(input())):
  w=input()
  for i in range(len(w)-1):
    if w[i]==w[i+1]:print(w[i]+w[i+1]);break
  else:
    for i in range(len(w)-1):
      if len(set(w[i:i+3]))==3:print(w[i:i+3]);break
    else:
      print(-1)

    