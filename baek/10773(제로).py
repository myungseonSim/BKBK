K = int(input())

A_arr =[]
for i in range(K):
    A = int(input())
    if A == 0:
        A_arr.pop()
    else:
        A_arr.append(A)
print(sum(A_arr))