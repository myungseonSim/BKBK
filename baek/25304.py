#영수증
total = int(input()) #영수증에 적힌 총 금액
count = int(input()) #영수증에 적힌 구매한 물건의 종류의 수
sum = 0 #계산금액 저장

for i in range(count): #물건의 종류의 수 만큼 반복
    price,Num = map(int,input().split()) #물건의 가격,개수 입력
    sum = sum+price*Num #물건을 계산
    
if sum == total: #총 금액과 계산한 금액이 같으면
    print("Yes") #Yes출력
else:
    print("No")