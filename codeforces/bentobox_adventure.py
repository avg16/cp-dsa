input_var = list(map(int,input().split()))
input_var.sort()
for i in range(1,6):
    if i not in input_var:
        print(i)
        break