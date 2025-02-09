import sys
input = sys.stdin.readline

n, k = map(int,input().split())

coin = [int(input()) for _ in range(n)]

cnt = 0

for i in reversed(coin):
    if k == 0:
        break
    cnt += k // i
    k %= i

print(cnt)