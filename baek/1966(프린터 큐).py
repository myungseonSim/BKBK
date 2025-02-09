import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    pri = list(map(int,input().split()))
    
    queue = deque([(pri[i], i) for i in range(N)]) #큐에 중요도와 원래위치를 한번에 저장 enumerate를 활용해도됨.
    print_order = 0
    
    while queue:
        current = queue.popleft()
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[1] == M:
                print(print_order)
                break