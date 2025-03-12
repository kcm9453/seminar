import sys

n = int(sys.stdin.readline()) # 이 부분이 입력 받을 때 입출력 속도에 따라서 런타임 오류가 발생 하여 input 대신 사용한다

stack = [] # 입력할 스택을 초기화 해준다.

for i in range(n):
    command = sys.stdin.readline().split() #커맨드에 input 함수 대신 사용

    if command[0] == 'push':
        stack.append(command[1]) # 커맨드 1이 입력 받을 경우 1스택이 추가가 된다

    elif command[0] == 'pop':
        if len(stack) == 0: #원소 개수가 0일 때 -1로 출력
            print(-1)
        else:
            print(stack.pop()) # 그렇지 않을 경우 삭제

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)