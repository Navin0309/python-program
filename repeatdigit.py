a = list(str(i) for i in range(int(input()),int(input())+1))
count = 0
for i in a:
    if len(set(i)) == len(i):
        count+= 1 
print(count)