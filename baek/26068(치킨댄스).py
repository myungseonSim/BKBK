import re

imo = int(input())
count = 0
for i in range(imo):
    day = input()
    a = int(re.sub(r"[^0-9]","", day))
    if(a <= 90):
        count+=1
print(count)