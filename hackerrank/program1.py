# Example
# x=1
# y=1
# z=2
# n=3
# All permutations of [i, j, k] are:
# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]].
# Print an array of the elements that do not sum to n = 3.
# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

a = int(input())
b = int(input())
c = int(input())
n = int(input())

result = [[i,j,k] for i in range (a+1) for j in range(b+1) for k in range(c+1) if a+b+c != n]
print(result)