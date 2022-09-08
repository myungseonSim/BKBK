#설탕배달
N = int(input()) #배달하려는 설탕 무게
count = 0

while N >= 0: #0보다 크면 반복
    if N % 5 == 0: #5로 나누었을때 나머지가 0이면
        count += int(N//5) #5로 나는 나머지를 저장
        print(count) #출력
        break #종료
    N -= 3 #5로 나눠서 안떨어지면 3을빼기
    count += 1 #1씩 저장
    
else:
    print(-1) #정확하게 N킬로그램을 만들 수 없다면 -1을 출력