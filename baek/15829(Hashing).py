L = int(input())
M = input()
N = 1234567891
S = 0

for i in range(L):
    S += (ord(M[i])-96) * (31**i)
print(S % N)