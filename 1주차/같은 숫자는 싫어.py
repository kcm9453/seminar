import sys  # sys 모듈을 가져옵니다. 표준 입력을 빠르게 처리하기 위해 사용됩니다.

# 첫 번째 줄에서 정수 n을 입력받습니다.
# 이는 입력될 명령어의 개수를 의미합니다.
n = int(sys.stdin.readline())

# 'push' 명령을 처리할 스택(리스트)을 생성합니다.
answer = []

# n개의 명령을 처리하기 위한 반복문을 실행합니다.
for i in range(n):
    # 한 줄을 입력받아 공백을 기준으로 분리합니다.
    # 예를 들어 "push 3"이 입력되면, ['push', '3'] 형태의 리스트가 됩니다.
    command = sys.stdin.readline().split()

    # 만약 첫 번째 요소가 'push'라면 (즉, push 명령어가 입력되었다면)
    if command[0] == 'push':
        # 스택이 비어 있거나, 스택의 최상단 값이 현재 입력값과 다를 경우에만 값을 추가합니다.
        # 이를 통해 연속된 중복 push를 방지합니다.
        if len(answer) == 0 or answer[-1] != command[1]:
            answer.append(command[1])  # 스택에 값을 추가합니다.

# 모든 명령 처리가 끝난 후, 스택의 최종 상태를 출력합니다.
print(answer)

# 부가 설명
# for i in range(n):                                        n은 첫 번째 입력에서 받은 숫자로, 실행할 명령어의 개수를 의미합니다.
#    command = sys.stdin.readline().split()                 예를 들어, 입력이 "push 3"이라면 command = ['push', '3'] 리스트가 됩니다.
#    if command[0] == 'push':
#        if len(answer) == 0 or answer[-1] != command[1]:
#            answer.append(command[1])
                                                            # answer는 리스트(스택 역할)이며, 여기에 값을 추가할지를 결정하는 조건문입니다.
                                                            # len(answer) == 0
                                                            # answer가 비어 있다면(answer = []), 즉 첫 번째로 추가하는 값이라면 무조건 추가합니다.
                                                            # answer[-1] != command[1]
                                                            # answer[-1]은 answer 리스트의 마지막 요소(스택의 최상단 값)를 의미합니다.
                                                            # command[1]는 입력받은 값(즉, push 뒤에 오는 숫자)입니다.
                                                            # 만약 answer[-1]과 command[1]가 다르면 새로운 값이므로 추가해야 합니다.
                                                            # 예를 들어, answer = ['1', '2']이고 command[1] == '2'라면, 마지막 값과 같으므로 추가하지 않습니다.
                                                            # 위 조건을 만족하면 command[1](즉, push 뒤에 오는 값)을 answer 리스트에 추가합니다.
                                                            # 즉, 스택의 맨 위에 새로운 값을 추가하는 동작입니다.