A_arr= []
for i in range(5):
    A = int(input())
    A_arr.append(A)
A_arr.sort()
avg = (sum(A_arr)/5)

print(int(avg))
print(A_arr[2])