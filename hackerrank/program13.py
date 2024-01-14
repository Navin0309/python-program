if __name__ == "__main__":
    s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    n = 4
    for i in range(0,len(s),n):
        substring = s[i:i+n]
        print(substring)