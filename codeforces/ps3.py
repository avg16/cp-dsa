
import sys

def solve():
    input = sys.stdin.readline
    t= int(input())
    for _ in range(t):
        n = int(input())
        gr = {}
        currencies = set()
        for _ in range(n):
            A,B,rate = input().split()
            rate = float(rate)
            currencies.add(A)
            currencies.add(B)
            if A not in gr:
                gr[A] = []
            gr[A].append((B,rate))
            if B not in gr:
                gr[B] = []
            gr[B].append((A, 1/rate))
        
        f= False
        sorted_currencies = sorted(currencies)
        for start in sorted_currencies:
            max_depth = len(sorted_currencies)
            for depth in range(2,max_depth+1):
                stack = [(start,1,[])]
                while stack:
                    curr,pr,path = stack.pop()
                    if curr== start and len(path) >= 1:
                        if len(path) + 1 > depth:
                            continue
                        if pr > 1.001:
                            cycle = path + [start]
                            print(' '.join(cycle))
                            f = True
                            break
                        else:
                            continue
                    if len(path) >= depth:
                        continue
                    for nb, rate in gr.get(curr, []):
                        if nb != start and nb in path:
                            continue
                        newpr = pr*rate
                        new_path = path+[curr]
                        stack.append((nb, newpr, new_path))
                    if f:
                        break
                if f:
                    break
            if f:
                break
        if f==False:
            print("NO")

solve()
