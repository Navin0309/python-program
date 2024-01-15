# Print the following 3 lines, each to 6 decimals:
# 1. proportion of positive values
# 2. proportion of negative values
# 3. proportion of zeros
# Sample Input
# STDIN
# Function
# 6
# arr[] size n = 6
# -43-9041 arr = [-4, 3, 9, 0, 4, 1]
# Sample Output
# 0.500000
# 0.333333
# 0.166667
# Explanation
# There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
# The proportions of occurrence are positive: 3 6 = 0.500000, negative: 2 = 0.333333 and zeros: 1 = 0.166667.

a = [-4, 3, -9, 0, 4, 1]
x=len(a)
n = []
m = []
l = []

for i in a:
    if i > 0:
        n.append(i)
    elif i < 0:
        m.append(i)
    elif i == 0:
        l.append(i)
print(len(n)/x)
print(len(m)/x)
print(len(l)/x)
