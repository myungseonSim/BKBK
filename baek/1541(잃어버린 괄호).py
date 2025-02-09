import sys
input = sys.stdin.readline

a = input().strip()

parts = a.split("-")

result = sum(map(int,parts[0].split('+')))

for part in parts[1:]:
    result -= sum(map(int,part.split('+')))
    
print(result)