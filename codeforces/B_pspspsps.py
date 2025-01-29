for _ in range(int(input())):
    n = int(input())
    s = input()
    if "s" in s[1:] and "p" in s[:n-1]:
        print("NO")
    else:
        print("YES")