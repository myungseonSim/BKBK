N = int(input()) #정수 입력
num = N #num에 정수 저장
count = 0 #반복횟수 저장

while True:
    a = num // 10 #2자리수 일때 앞자리 구하기
    b = num % 10 #2자리 수일때 뒷자리 구하지
    c = (a + b) % 10 #앞자리 뒷자리 더한후 뒷자리만 구하기 
    num = (b * 10) + c #b를 앞자리로 바꾼후 c로 뒷자리 더하기
    
    count+=1 #반복횟수 증가
    if (num == N): #처음 입력받은 정수와 같아지면 종료
        break
    
print(count)