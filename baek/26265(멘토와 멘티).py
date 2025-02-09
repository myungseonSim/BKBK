import sys
input = sys.stdin.readline

n = int(input())
k = [input().split() for _ in range(n)]

# 멘티 내림차순 정렬
k.sort(key=lambda x: x[1], reverse=True)

# 멘토 오름차순 정렬
k.sort(key=lambda x: x[0])

# 출력
for mentor, mentee in k:
    print(mentor, mentee)

