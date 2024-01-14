# Sample Input

# ABCDCDC
# CDC
# Sample Output

# 2

# def count_substring(string,sub_string):
#     count = 0
#     for i in range(len (string)):
#         if string[i:len(string)].startswith(sub_string):
#             count+=1
#     return count
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     count = count_substring(string, sub_string)
#     print(count)

a = input()
b = input()

count  = 0
for i in range(len(a)):
    if a[i:len(a)].startswith(b):
        count+=1
print(count) 