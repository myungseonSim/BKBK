import sys

def push(item):
    stack.append(item)
def pop():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack.pop())
def size():
    print(len(stack))
def empty():
    if len(stack) == 0:
        print("1")
    else:
        print("0")
def top():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[-1])
        
        
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if(command[0] == 'push'):
        push(command[1])
    if (command[0] == 'pop'):
        pop()
    if (command[0] == 'size'):
        size()
    if (command[0] == 'empty'):
        empty()
    if (command[0] == 'top'):
        top()