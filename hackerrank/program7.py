# Sample Input

# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# Sample Output

# abrackdabra


s = input()
p,c = input().split()
position = int(p)
result = s[:position] + c + s[position + 1:]
print(result)

# def mutate_string(string, position, character):
#     result = string[:position] + character + string[position + 1:]
#     return result

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)