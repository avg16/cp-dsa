n = int(input())
arr = list(map(int, input().split()))

ev=[]
od=[]
for i in arr:
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)
if len(ev)==1:
    print(arr.index(ev[0]) +1)
elif len(od)==1:
    print(arr.index(od[0]) + 1)

# if len(ev)>len(od):
#     print(od[0])
# else:
#     print(ev[0])



    


