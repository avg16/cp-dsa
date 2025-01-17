def calculate_perimeter(n, m, moves):
    from collections import defaultdict

    colored_cells = set()

    def fill_square(x, y):
        for i in range(m):
            for j in range(m):
                colored_cells.add((x + i, y + j))
    curr_x, curr_y = 0, 0
    for x_move, y_move in moves:
        curr_x += x_move
        curr_y += y_move
        fill_square(curr_x, curr_y)

    perimeter = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    
    for cell in colored_cells:
        x, y = cell
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor not in colored_cells:
                perimeter += 1
    
    return perimeter

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        moves = []
        for _ in range(n):
            x, y = map(int, input().split())
            moves.append((x, y))
        print(calculate_perimeter(n, m, moves))

if __name__ == "__main__":
    solve()

