import sys
input = sys.stdin.readline

n = int(input())
names = [input().strip() for _ in range(n)]

ln = len(names)
cnt = 0

for i in range(ln):
    for j in range(i+1, ln):
        s, t = names[i], names[j]
        
        min_lenght = min(len(s), len(t))
        for k in range(1, min_lenght + 1):
            if s[:k] == t[-k:] or s[-k:] == t[:k]:
                cnt += 1
                break

print(cnt)