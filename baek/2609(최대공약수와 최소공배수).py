A, B = map(int,input().split())
a, b = A, B

while b != 0: #유클리드 호제법
    a = a % b
    a, b = b, a
    
print(a) #최대공약수
print(A*B//a) #최소공배수

"""
import math #파이썬 내장함수
a, b = map(int, input().split())
print(math.gcd(a,b))
print(math.lcm(a,b))
"""