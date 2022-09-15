from re import A
import string

S = input()

a = 'abcdefghijklmnopqrstuvwxyz'

for i in a:
    print(S.find(i), end = (" "))