n = int(input())
arr = list(map(int, input().split()))

max_len = 0
max_seq = []

for i in range(n):
    seq = []
    req = 1
    for j in range(i, n):
        if arr[j] == req:
            seq.append(2001 + j)
            req += 1
    if len(seq) > max_len:
        max_len = len(seq)
        max_seq = seq

if max_len == 0:
    print(0)
else:
    print(max_len)
    print(' '.join(map(str, max_seq)))