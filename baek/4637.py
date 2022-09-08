#셀프넘버
def d(N):
    N = N + sum(map(int,str(N)))
    return N

nonSelfNum = set()

for i in range(1,10001):
    nonSelfNum.add(d(i))
for j in range(1,10001):
    if j not in nonSelfNum:
        print(j)