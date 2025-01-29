
import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n, k = int(data[index]), int(data[index + 1])
        arr = map(int, data[index + 2:index + 2 + n])
        index += 2 + n
        
        pair_potential = defaultdict(int)
        score = 0
        
        for num in arr:
            complement = k - num
            if pair_potential[complement] > 0:
                score += 1
                pair_potential[complement] -= 1
            else:
                pair_potential[num] += 1
        
        results.append(score)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
