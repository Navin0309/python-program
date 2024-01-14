a=int(input())
b=list(map(int,input().split()))
m=max(b)
c=0
i=b.index(m)
while(m>0):
  c+=1
  for l in range(i,a):
    b[l]= 0
  m=max(b)
  i=b.index(m)
print(c)
