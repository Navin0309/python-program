# Input Format
# The first line contains Integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m Integers, A and B, respectively.
# Output Format
# Output a single integer, your total happiness.
# Sample Input
# 32
# 153
# 31
# 57
# Sample Output
# 1
# Explanation
# You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B
# does not exist in the array so it is not included in the calculation.
# Hence, the total happiness is 2-1=1.

a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))

A = set(map(int, input().strip().split(' ')))
B = set(map(int, input().strip().split(' ')))
happiness = 0
for i in b:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
print(happiness)
    
    
