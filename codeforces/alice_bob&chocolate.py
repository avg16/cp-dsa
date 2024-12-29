n = int(input())
arr = list(map(int, input().split()))
alice_time = 0
bob_time = 0
alice = 0
bob = 0

from sys import stdin,stdout
i,j = 0,n-1
while i<=j:
    if alice_time<=bob_time:
        alice_time+=arr[i]
        alice+=1
        i+=1
    else:
        bob_time+=arr[j]
        bob+=1
        j-=1

print(alice, bob)