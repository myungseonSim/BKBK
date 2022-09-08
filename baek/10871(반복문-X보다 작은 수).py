#X보다 작은 수
N,X = map(int,input().split()) #정수의 개수와 최소값의 기준을 입력
A = list(map(int,input().split())) #수열을 만듬

for i in range(N): #N-1번 반복
    if A[i]<X: #최솟값보다 작은 수열의 수면
        print(A[i],end=' ') #출력