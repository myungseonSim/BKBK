A, B = map(int,input().split())

max_v = max(A,B)
min_v = min(A,B)

sum = (A+B) * (max_v - min_v +1)/2
print(int(sum))