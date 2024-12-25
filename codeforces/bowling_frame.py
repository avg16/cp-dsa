def max_triangle_side(w, b):
    def can_form_triangle(s, w, b):
        for row in range(1, s + 1):
            if w >= row:
                w -= row
            elif b >= row:
                b -= row
            else:
                return False
        return True

    low, high = 0, int((2 * (w + b)) ** 0.5) + 1
    while low < high:
        mid = (low + high + 1) // 2
        if can_form_triangle(mid, w, b):
            low = mid
        else:
            high = mid - 1

    return low


t = int(input())
results = []
for _ in range(t):
    w, b = map(int, input().split())
    results.append(max_triangle_side(w, b))
    
for res in results:
    print(res)