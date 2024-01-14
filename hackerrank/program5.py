# Sample Input 0

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0

# 56.00
# Explanation 0

# Marks for Malika are {52+56+60}/3 whose average is 56 


n = []
for _ in range(int(input())):
    input_data = input().split()
    name = input_data[0]
    marks = list(map(float, input_data[1:]))
    n.append([name, marks])

student_name = input()
m = list(next(i for i in n if i[0] == student_name))
average = sum(m[1]) / len(m[1])
print("{:.2f}".format(average))
