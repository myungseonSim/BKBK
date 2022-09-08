N = int(input()) #숫자 N개 받기
nums = input() #숫자들을 저장
total = 0 #숫자들의 합을 저장

for i in range (N): #N-1번 반복
    total += int(nums[i]) #i~N까지 더해서 저장
print(total) #출력
