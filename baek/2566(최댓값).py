import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(list(map(int,input().split())))
        
x = 0
y = 0
max_num = -1

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = arr[i][j]
            x = i + 1
            y = j + 1
            
print(max_num)
print(x,y)