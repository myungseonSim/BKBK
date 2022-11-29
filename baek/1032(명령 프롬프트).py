N = int(input())

A_arr = list(input())
A_len = len(A_arr)

for i in range(N-1):
    B_arr = list(input())
    for j in range(A_len):
        if A_arr[j] != B_arr[j]:
            A_arr[j] ='?'
print(''.join(A_arr))