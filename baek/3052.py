arr = [] #배열을 만들어줌
for i in range(10):
    A = int(input())
    B = A % 42
    arr.append(B) #배열에 42로 나눈 나머지를 넣어줌
    
arr = set(arr) #set함수로 중복을 제거
print(len(arr)) #중복을 제거한 갯수 반환