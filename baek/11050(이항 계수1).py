N, K = map(int,input().split())

def facto(N): #nCk로 나타낼수 있음
    if N == 0 :
        return 1
    return (N * facto(N-1))

print(facto(N) // (facto(K) * facto(N-K)))