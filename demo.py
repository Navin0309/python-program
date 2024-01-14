# n = []
# for _ in range(int(input())):
#     a = input()
#     b = float(input())
#     c = int(input())
#     n.append([a, b, c])

# n.sort(key=lambda x: (x[2], x[1], x[0]))
# for i in n:
#     if i == n[1]:
#         print(n[1])


s = input()
p,c = input().split()
position = int(p)
result = s[:position] + c + s[position + 1:]
print(result)

def mutate_string(string, position, character):
    result = string[:position] + character + string[position + 1:]
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
