# Sample Input

# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
# Sample Output

# 5
# 9
# 11
a = int(input())
a1 = set(map(int, input().split()))
b = int(input())
b1 = set(map(int, input().split()))
n = a1.difference(b1)
m = b1.difference(a1)
c = n.union(m)
for i in sorted(c):
    print(i)

