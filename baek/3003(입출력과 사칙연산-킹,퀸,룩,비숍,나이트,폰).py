#킹,퀸,룩,비숍,나이트,폰
K = [1,1,2,2,2,8] #킹,퀸,룩,비숍,나이트,폰의 총개수를 저장

c = list(map(int, input().split()))#킹,퀸,룩,비숍,나이트,폰의 현재개수를 입력

for i in range(6):
    print(K[i]-c[i],end=' ') #총개수에서 현재개수를 빼어 부족한 수를 출력 