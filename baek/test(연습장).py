M, N = map(int,input().split())

for i in range(M,N+1):
    if i == 1:
        continue
    print(int(i**0.5)+1)
    