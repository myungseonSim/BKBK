N = int(input())

A = map(int,input().split(' '))
cnt = 0

for i in A:
    check = 0
    if i == 1:
        continue
    for j in range(2,i+1):
        if i%j == 0:
            check += 1
            
    if check == 1:
        cnt += 1
        
print(cnt)
        