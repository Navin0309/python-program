s = "AABCAAADA"
k = 3

n = len(s)
for i in range(0, n, k):
    substring = s[i:i+k]
    unique_substring = ''.join(sorted(set(substring), key=substring.index))
    print(unique_substring)
