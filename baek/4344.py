C = int(input()) #반복할 횟수 입력

for i in range(C):
    nums = list(map(int,input().split())) #점수를 list형태로 저장
    avg = sum(nums[1:])/nums[0] 
    #배열의 0번은 학생수고 1번부터 점수이므로 sum함수로 점수를 다 더한후 학새수로 나누어 평균을 구함
    cnt = 0 #점수가 평균을 넘는 학생 카운트
    for j in nums[1:]:
        if (j>avg):
            cnt += 1
    rate = (cnt/nums[0])*100 #평균을 넘는 학생수를 기존학생수로 나눈다음 100을 곱함 비율구하기
    print(f'{rate:.3f}%') #f-string을 이용하여 소수점 셋째 자리까지 출력