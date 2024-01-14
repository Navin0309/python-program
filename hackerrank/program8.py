# Task
# Given an Integer, n, and n space-separated Integers as input, create a tuple, t, of thosen integers. Then compute and print the result of hash(t).
# Note: hash() is one of the functions in the__builtins__ module, so it need not be imported.
# Input Format
# The first line contains an Integer, n, denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t.
# Output Format
# Print the result of hash(t).
# Sample Input 0
# 2
# 12
# Sample Output 0
# 3713081631934410656

a = int(input())
b = tuple(map(int,input().split()))
print(hash(b))

# khdf
# sf