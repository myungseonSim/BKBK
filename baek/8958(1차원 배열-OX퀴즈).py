N = int(input()) #반복할 횟수 입력

for i in range(N):
    ox_list = list(input()) #OX를 입력받아 저장할 변수
    count = 0 #O가 나왔을때 점수 추가
    sum_count = 0 #총합 점수
    for j in ox_list:
        if(j == 'O'): #O가 있을때 1점 추가후 점수 합산
            count += 1
            sum_count += count
        else:
            count = 0
    print(sum_count)
    