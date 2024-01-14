
def merge_the_tools(string,k):
    n=[]
    for i in range(0,len(string),k):
        m =string[i:i+k]
        unique = ''.join(dict.fromkeys(m))
        n.append(unique)
    for j in n:
        print(j)
if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)

