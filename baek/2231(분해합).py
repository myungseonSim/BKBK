N = int(input())
result = 0

for i in range(1, N+1):
    A = list(map(int,str(i)))
    s = i + sum(A)
    if(s == N):
        result = i 
        break
    
print(result)