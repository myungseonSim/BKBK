#최댓값
data = [] #자연수들을 저장하기 위한 배열
for i in range(9):
    data.append(int(input())) #9개의 자연수를 차례대로 저장
print(max(data)) #최댓값 출력
print(data.index(max(data))+1) #최댓값이 몇번째 수인지 출력
