T = int(input())

for _ in range(T):
    N, P = map(int, input().split())
    result = N % P  
    print(result)
