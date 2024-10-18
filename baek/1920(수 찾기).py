import sys
input = sys.stdin.readline
N = int(input())
N_list = set(map(int,input().split())) #set함수는 내부적으로 해시 테이블을 사용하여 in 연산을 평균 O(1)시간복잡도
M = int(input())
M_list = list(map(int,input().split()))


for i in M_list:
    if i in N_list:
        print(1)
    else:
        print(0)