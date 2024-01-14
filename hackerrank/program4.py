# 2
# navin
# 23.4
# 3
# kumar
# 24.5
# 4
# ['kumar', 24.5, 4]

n = []
for _ in range(int(input())):
    a = input()
    b = float(input())
    c = int(input())
    n.append([a, b, c])
n.sort(key=lambda x: (x[2], x[1], x[0]))
for i in n:
    if i == n[1]:
        print(n[1])
