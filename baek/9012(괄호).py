T = int(input())

for _ in range(T):
    N = input()
    M = list(N)
    sum = 0
    
    for i in M:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
                        