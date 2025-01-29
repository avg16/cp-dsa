for _ in range(int(input())):
	n, m, q = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	dic = {}
	j = 0
	ok = True
	for i in b:
		if i not in dic:
			if i != a[j]:
				ok = False
				break
			else:
				j += 1
				dic[i] = 1	 
	
	print("YA" if ok else "TIDAK")