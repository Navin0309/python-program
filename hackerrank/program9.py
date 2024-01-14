# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    n=s.swapcase()
    return n

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
