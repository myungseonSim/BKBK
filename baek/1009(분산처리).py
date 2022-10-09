import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int,input().split())
    AA = A%10
    
    if AA == 0:
        print(10)
    elif AA in [1,5,6]:
        print(AA)
    elif AA in [4,9]:
        BB = B%2
        if BB == 0:
            print(AA*AA%10)
        else:
            print(AA)
    else:
        BB =B%4
        if BB == 0:
            print(AA**4%10)
        else:
            print(AA**BB%10)
    