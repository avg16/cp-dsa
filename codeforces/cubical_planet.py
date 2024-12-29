x1,y1,z1= map(int,input().split())
x2,y2,z2= map(int,input().split())

def distance(x1,y1,z1,x2,y2,z2):
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

if distance(x1,y1,z1,x2,y2,z2) == (3)**0.5:
    print('NO')
else:
    print('YES')