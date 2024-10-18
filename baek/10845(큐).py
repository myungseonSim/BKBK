import sys

def push(item):
    que.append(item)
def pop():
    if len(que) == 0:
        print("-1")
    else:
        print(que.pop(0))
def size():
    print(len(que))
def empty():
    if len(que) == 0:
        print("1")
    else:
        print("0")
def front():
    if len(que) == 0:
        print("-1")
    else:
        print(que[0])
def back():
    if len(que) == 0:
        print("-1")
    else:
        print(que[-1])
        
        
N = int(sys.stdin.readline())
que = []

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if(command[0] == 'push'):
        push(command[1])
    elif (command[0] == 'pop'):
        pop()
    elif (command[0] == 'size'):
        size()
    elif (command[0] == 'empty'):
        empty()
    elif (command[0] == 'front'):
        front()
    elif (command[0] == 'back'):
        back()