import sys
input = sys.stdin.readline

n = int(input())

people = list(map(int,input().split()))

t, p = map(int,input().split())

cnt = 0

#티셔츠
for i in people:
    if i == 0:
        continue
    elif i <= t:
        cnt += 1
    elif i % t == 0:
        cnt += (i//t)
    else:
        cnt += (i//t) + 1

print(cnt)
print(n//p,n%p)