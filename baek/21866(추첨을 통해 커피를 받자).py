max_score = [100,100,200,200,300,300,400,400,500]
arr = list(map(int,input().split()))
c = 0
is_hacker = False #해커인지 여부 판단 0,1로 구분하여도 됨
for i in range(9):
    if arr[i] > max_score[i]: #점수가 초과되면 해커로 지정
        is_hacker = True
        break
    c+=arr[i] #점수의 합산
        
if is_hacker:
    print("hacker")

else:
    if c < 100:
        print("none")
    else:    
        print("draw")