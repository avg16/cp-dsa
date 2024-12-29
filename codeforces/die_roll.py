y,w = map(int,input().split())
chance = 0
for i in range(1,7):
    if i==max(y,w):
        chance+=1
    elif i > y and i>w:
        chance+=1
def simplify_fraction(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    if a == 0:
        return 0, 1
    if a < 0 and b < 0:
        a, b = -a, -b
    elif a < 0 or b < 0:
        a, b = -a, b
    gcd = gcd_euclid(a, b)
    return print(f"{a // gcd}/{b // gcd}")

def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a
simplify_fraction(chance,6)