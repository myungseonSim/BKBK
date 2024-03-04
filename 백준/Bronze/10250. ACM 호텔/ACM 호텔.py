T = int(input())
#층. 방수, 번째
for i in range(T):
  H,W,N = map(int,input().split())

  num = N % H
  line = (N//H)+1
  if num ==0:
    num = H
    line -= 1

  print(num * 100 + line)  
