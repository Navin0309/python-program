a = int(input('ENTER THE INPUT:'))
n=[]
for i in range(1, a + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        n.append(i)
print(n)
