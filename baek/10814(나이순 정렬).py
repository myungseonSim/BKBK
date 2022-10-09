N = int(input())

m_list = []

for _ in range(N):
    age, name = map(str,input().split())
    age = int(age)
    m_list.append((age,name))

m_list.sort(key = lambda x : x[0])

for i in m_list:
    print(i[0],i[1])