# Sample Input 0
# 5
# 2
# 3
# 65
# 6
# Sample Output 0
# 5
# Explanation 0
# Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum Is 5. Hence, we print 5 as the runner-up score.

a = int(input())
b = map(int,input().split())

duplication = list(set(b))
result = sorted(duplication,reverse=True)
print(result[1])