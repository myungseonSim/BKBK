import sys
input = sys.stdin.readline

n, m = map(int,input().split())

hear = set()
see = set()

for _ in range(n):
    hear.add(input().strip())
    
for _ in range(m):
    see.add(input().strip())

ans = sorted(hear & see)

print(len(ans))
for x in ans:
    print(x)