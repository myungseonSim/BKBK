A = int(input())
B = int(input())

C = (B % 100) #85
D = (C % 10) #5
E = (C // 10) #8
F = (B // 100) #3

print(A*D)
print(A*E)
print(A*F)
print(A*B)