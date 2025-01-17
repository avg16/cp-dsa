n=int(input())
x=1;
while int(bin(x)[2:]) <= n:
    # print(x,end=" ");print(int(bin(x)[2:]))
    x+=1
print(x-1)