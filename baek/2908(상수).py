A, B = map(int,input().split())

C = str(A)[::-1]
D = str(B)[::-1]

print(max(C,D))