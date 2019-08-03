from collections import Counter

m = int(input())
a = []
b = input().split()
for i in range(0,m):
	a.append(b[i])

results = Counter(a)
c = []
#print(results)
for i in results:
	if(results[i]>1):
		c.append(i)
c = sorted(c)
if not c:
	print("unique")
else:
	print(" ".join(c))
