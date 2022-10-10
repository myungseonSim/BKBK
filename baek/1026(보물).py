N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

S = 0
A.sort()
for i in range(N):
    x = A[i]
    y = B.pop(B.index(max(B)))
    S += x * y
    
print(S)
    
        