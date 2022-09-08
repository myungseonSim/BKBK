#달팽이는 올라가고 싶다
A,B,V = map(int, input().split()) #높이,상승,하강 변수입력
k = (V-B)/(A-B) #도달하기까지 일수
#도달하면 끝나기 때문에 낮에 끝난다는 가정하에 B를 한번 빼줌

if k==int(k): #정수형으로 떨어지면 그대로
    print(int(k)) 
else: #그렇지 않으면 1을 추가
    print(int(k)+1)
    