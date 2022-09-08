#A+B-5
while 1:
    A,B = map(int,input().split()) #정수 A,B를 입력받음
    if A ==0&B==0: #만약 A랑B가 0이면 종료
        break
    print(A+B) #그렇지 않으면 출력