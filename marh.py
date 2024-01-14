import math
a = int(input())
k = int(input())
n = []
m = []
m1 = []
for i in range(a):
    b = int(input())
    n.append(b)
for j in n:
        m.append(j//k)
for u in n:
        m1.append(u//k-1)
f=math.gcd(*m1)
if f == 1:
    print('yes')
else:
    print('no')
