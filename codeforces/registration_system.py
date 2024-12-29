n = int(input())
pp_set = {}
results = []

for _ in range(n):
    pp = input()
    if pp not in pp_set:
        pp_set[pp] = 1
        results.append('OK')
    else:
        pp_set[pp] += 1
        results.append(pp + str(pp_set[pp]-1))

for res in results:
    print(res)