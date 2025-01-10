t = int(input())
for _ in range(t):
    n = int(input())
    num_of_lens = {}
    for _ in range(n):
        x = int(input())
        num_of_lens[x] = num_of_lens.get(x, 0) + 1

    res = 0
    total = 0
    for cnt in num_of_lens.values():
        if cnt >= 3:
            res += cnt * (cnt - 1) * (cnt - 2) // 6
        if cnt >= 2:
            res += cnt * (cnt - 1) // 2 * total
        total += cnt

    print(res)
