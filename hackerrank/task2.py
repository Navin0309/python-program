a = [1,2,3,4,5]
n=[]
for i in range(len(a)):
    b=a[:i]+a[i+1:]
    m=sum(b)
    n.append(m)
print(max(n))