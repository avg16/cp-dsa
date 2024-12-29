# def can_unlock(x):
#     while x > 0:
#         x_str = str(x)
#         if '33' in x_str:
#             index = x_str.find('33')
#             x_str = x_str[:index] + x_str[index + 2:]
#             x = int(x_str) if x_str else 0
#         elif x >= 33:
#             x -= 33
#         else:
#             return "NO"
#     return "YES" if x == 0 else "NO"
def can_unlock(x):
    return 'YES' if x%33==0 else 'NO'

t = int(input())
test_cases = []
for _ in range(t):
    x = int(input())
    test_cases.append(x)

results = []
for x in test_cases:
    results.append(can_unlock(x))

for res in results:
    print(res)