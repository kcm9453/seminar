import sys                                  # sys 모듈이 입출력 속도를 높여줌
n = int(sys.stdin.readline())               # 이 부분이 입력 받을 때 입출력 속도에 따라서 런타임 오류가 발생 하여 input 대신 사용한다

stack = []                                  # 입력할 스택을 초기화 해준다.

for i in range(n):                          # n개의 명령어를 차례 대로 입력 받아 처리함
    command = sys.stdin.readline().split()  # 한 줄을 입력 받고 공백을 기준 으로 잡아 분리 하여 리스트로 저장

    if command[0] == 'push':
        stack.append(command[1])            # push 명령어는 command[1]에 들어 있는 상수 x값을 stack 뒤쪽 으로 추가

    elif command[0] == 'pop':
        if len(stack) == 0:                 # pop 스택의 원소 개수가 0일 때 -1로 출력
            print(-1)
        else:
            print(stack.pop())              # 그렇지 않을 경우 삭제

    elif command[0] == 'size':              # size가 스택 안에 있는 요소의 개수를 출력 시켜 줌
        print(len(stack))

    elif command[0] == 'empty':             # empty
        if len(stack) == 0:
            print(1)                        # 스택의 원소 함수의 개수가 0일 경우 1이 반환이 되고
        else:
            print(0)                        # 그렇지 않으면 0으로 출력 한다.

print(stack)