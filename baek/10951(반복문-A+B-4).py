#A+B-4 
while True: #참일때 계속 반복
    try: 
        #try에서 오류가 발생하면 except로 넘어감 발생하지않으면 계속실행
        A,B = map(int,input().split())
        print(A+B)
    except:
        break

