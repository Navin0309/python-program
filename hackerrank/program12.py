a = 'qA2'
for i in a:
    if i.isalpha():
        print('True')
        break
for j in a:
    if j.isdigit():
        print("True")
        break


# anothod method
# if __name__ == '__main__':
#     s = input()
#     print(any(map(str.isalnum, s)))
#     print(any(map(str.isalpha, s)))
#     print(any(map(str.isdigit, s)))
#     print(any(map(str.islower, s)))
#     print(any(map(str.isupper, s)))