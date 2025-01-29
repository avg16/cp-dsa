def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        v = list(map(int, data[index:index + n])) 
        index += n
        
        flag = True
        for i in range(n - 1):
            x = min(v[i], v[i + 1])
            v[i] -= x
            v[i + 1] -= x
            if v[i] > v[i + 1]:
                flag = False
                break
        
        if flag:
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
