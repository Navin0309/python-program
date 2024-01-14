# Sample Input

#  1 2
#  3 4
# Sample Output

#  (1, 3) (1, 4) (2, 3) (2, 4)

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

result = [(x, y) for x in list1 for y in list2]
output = " ".join(map(str, result))

print(output)
