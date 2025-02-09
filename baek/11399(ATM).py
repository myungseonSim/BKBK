import sys
input = sys.stdin.readline

answer = 0

n = int(input())
k = sorted(list(map(int,input().split())))

for i in range(1,n+1):
    answer += sum(k[0:i])
print(answer)