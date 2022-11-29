import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(map(int,input().split()))
result =[0]
temp = 0

for k in nums:
    temp += k
    result.append(temp)
    
for _ in range(M):
    i,j = map(int,input().split())
    print(result[j] - result[i - 1])
