import sys

N, M= map(int,sys.stdin.readline().split())

A_arr = []
B_arr = []
for _ in range(N):
    A_arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    B_arr.append(list(map(int,sys.stdin.readline().split())))
    
for row in range(N):
    for col in range(M):
        print(A_arr[row][col] + B_arr[row][col], end = ' ')
    print()
