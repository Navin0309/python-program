#https://codersdaily.in/courses/hacker-rank-solution/python-lists-hackerRank-solution

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
# [6, 5, 10]

# [1, 5, 9, 10]

# [9, 5, 1]

a = int(input())
b = []
for i in range(a):
    n = input().split()
    if n[0] == 'insert':
        b.insert(int(n[1]), int(n[2]))
    elif n[0] == 'remove':
        b.remove(int(n[1]))
    elif n[0] == 'append':
        b.append(int(n[1]))
    elif n[0] == 'sort':
        b.sort()
    elif n[0] == 'pop':
        b.pop()
    elif n[0] == 'reverse':
        b.reverse()
    elif n[0]=='print':
        print(b)