import sys
from collections import deque

n, k = map(int,input().split())
q = deque()

answer = []

for i in range(1,n+1):
    q.append(i)
    
while q:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())

print("<", end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")