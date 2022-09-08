#부녀회장이 될테야
T = int(input()) #테스트 케이스입력

for _ in range(T): #T만큼 반복
    f = int(input()) #층의 수를 입력받음
    n = int(input()) #호실의 수를 입력받음
    
    p = [i for i in range(1,n+1)] #0층의 사람들을 저장
    for x in range(f): #층의 수만큼 반복
        for j in range(1,n): #1호부터 호실의 수만큼 반복
            p[j] += p[j-1] #층별 호실의 사람수를 변경
    print(p[-1]) #가장 마지막 수 출력
