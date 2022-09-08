A = list(map(int,input().split()))

if A==sorted(A): #sorted() 오름차순 정렬
    print("ascending")
elif A == sorted(A, reverse=True): #sorted(list,reverse=True) 내림차순 정렬
    print("descending")
else:
    print("mixed")