import sys
input = sys.stdin.readline

K = int(input())
arr = [[0 for _ in range(101)]for _ in range(101)]

for _ in range(K):
    A,B = map(int,input().split())
    for i in range(A,A+10):
        for j in range(B,B+10):
            arr[i][j] = 1

num = 0
for N in arr:
    num += sum(N)       
print(num)