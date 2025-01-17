def can_alice_win(n, a, b):
    if abs(a - b) % 2 == 0:
        return "YES"
    else:
        return "NO"

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n, a, b = map(int, input().split())
        results.append(can_alice_win(n, a, b))
    print("\n".join(results))


if __name__ == "__main__":
    solve()