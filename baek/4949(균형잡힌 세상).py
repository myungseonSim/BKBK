while True:
    K = input()
    if K == '.':
        break
    arr = []
    temp = True
    for i in K:
        if i == '(' or i == '[':
            arr.append(i)
        elif i == ')':
            if not arr or arr[-1] == '[':
                temp = False
                break
            elif arr[-1] == '(':
                arr.pop()
        elif i == ']':
            if not arr or arr[-1] == '(':
                temp = False
                break
            elif arr[-1] == '[':
                arr.pop()
    if temp == True and not arr:
        print("yes")
    else:
        print("no")