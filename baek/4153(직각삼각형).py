while True:
    x = list(map(int,input().split()))
    m_num = max(x)
    if sum(x) == 0:
        break
    x.remove(m_num)
    if x[0]**2 + x[1]**2 == m_num**2:
        print("right")
    else:
        print("wrong")