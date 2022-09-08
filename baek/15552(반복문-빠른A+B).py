#빠른 A+B
import sys
N = int(input())

for i in range(N):
    A,B = map(int,sys.stdin.readline().split()) 
    #시간초과 없이 입력받기
    print(A+B)