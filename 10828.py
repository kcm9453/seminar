import sys

n = int(sys.stdin.readline()) # 이 부분이 입력 받을 때 입출력 속도에 따라서 런타임 오류가 발생 하여 input 대신 사용

stack = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)