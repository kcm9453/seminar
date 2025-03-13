from collections import deque           # deque collections 모듈에서 제공하는 자료구조이며 양쪽 끝에서 삽입과 삭제가 O(1)의 시간 복잡도로 빠르게 수행한다.

import sys                              # sys 모듈이 입출력 속도를 높여줌

input = sys.stdin.readline              # sys.stdin.readline 을 input으로 재 정의하여, 빠른 입력을 받을 수 있도록 한다.
n = int(input())                        # n은 명령어 개수를 의미하며, 정수를 변환하여 저장 시킨다.(리스트 형식으로 저장)
dq = []                                 # deque 를 입력할 요소를 초기화 해줌.

for _ in range(n):                      # n개의 명령어를 차례대로 입력 받아 처리한다. ex) command = ["push", "10"]
    command = list(input().split())     # 한 줄 입력 받고 공백을 기준으로 잡아서 분리하여 리스트로 저장시킴.

    if command[0] == 'push':            # push 명령어는 command[1]에 들어있는 x값을 dq 뒤쪽으로 추가합니다.
        dq.append(command[1])           # ex) push 10 을 입력하면 dq.append("10")이 실행이 되어 dq = [10]

    elif command[0] == 'pop':           # pop 명령어는 덱의 앞에서 값을 제거하고나서 출력하는 함수
        if len(dq) == 0:                # dq가 비어있으면 0 그렇지 안 ㅎ으면 -1로 출력시켜준다.
            print(-1)
        else : print(deque.pop(0))      # 덱이 0자릿수로 출력해준다.

    elif command[0] == 'size':          # size 명령어는 덱에 있는 요소의 개수를 출력해줌
        print(len(dq))                  # len(dq)를 사용하면 O(1)의 시간 복잡도로 크기를 알 수 있다.

    elif command[0] == 'empty':         # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(dq) > 0: print(0)
        else : print(1)

    elif command[0] == 'front':         # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(dq) > 0: print(dq[0])
        else : print(-1)

    elif command[0] == 'back':          # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(dq) > 0: print(dq[-1])
        else: print(-1)

print(dq)