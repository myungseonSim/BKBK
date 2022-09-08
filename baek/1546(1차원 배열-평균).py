#평균
N = int(input()) #새로운 평균
data = list(map(int,input().split())) #리스트 형태로 저장
max_score = max(data) #최대값 저장

new_data = []
for i in data:
    new_data.append(i/max_score*100) #append함수로 새로운 수를 맨끝에 저장
    
print(sum(new_data)/N) #출력