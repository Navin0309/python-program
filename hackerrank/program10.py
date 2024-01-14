# Sample Input
# this is a string  
 
# Sample Output
# this-is-a-string

def split_and_join(line):
    word = line.split()
    new = "-".join(word)
    return new

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# anothor method
# print('-'.join(input().split()))
