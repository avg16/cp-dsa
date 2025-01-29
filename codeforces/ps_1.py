import numpy as np
def neg_log_gr(tc):
    results = []
    for case in tc:
        ed = []
        curr = set()
        for pairs in case:
            ccy1,ccy2,rate = pairs
            rate = float(rate)
            ed.append((ccy1,ccy2, -np.log(rate)))
            curr.add(ccy1)
            curr.add(ccy2)
            if (ccy2,ccy1) not in [(e[0], e[1]) for e in ed]:
                ed.append((ccy2,ccy1,-np.log(1/rate)))
        res = []
        for edge in ed:
            ccy1,ccy2,w= edge
            res.append(f"{ccy1} {ccy2} {round(w, 6)}")
        results.append(res)
    return results

def solve():
    tc = []
    T = int(input())
    for _ in range(T):
        N = int(input())
        case = []
        for _ in range(N):
            line = input().strip().split()
            case.append((line[0],line[1],line[2]))
        tc.append(case)
    results = neg_log_gr(tc)
    for result in results:
        for line in result:
            print(line)
        print()


import sys
input = sys.stdin.readline

solve()