import sys  # sys 모듈을 사용하여 입력 속도를 향상시킵니다.

# 초기 문자열을 입력받아 왼쪽 스택(l_stack)에 저장합니다.
l_stack = list(sys.stdin.readline().strip())  # 커서 왼쪽에 있는 문자들을 저장하는 스택
r_stack = []  # 커서 오른쪽에 있는 문자들을 저장하는 스택

# 명령어 개수 n을 입력받습니다.
n = int(sys.stdin.readline().strip())

# n개의 명령을 차례로 처리합니다.
for _ in range(n):
    # 명령어를 입력받고 공백을 기준으로 나눕니다.
    command = sys.stdin.readline().split()

    # "L" 명령어: 커서를 왼쪽으로 이동
    if command[0] == 'L':
        # l_stack(왼쪽 스택)이 비어 있지 않다면, 왼쪽 끝 문자를 r_stack으로 이동
        if len(l_stack) >= 1:
            r_stack.append(l_stack.pop())

    # "D" 명령어: 커서를 오른쪽으로 이동
    elif command[0] == 'D':
        # r_stack(오른쪽 스택)이 비어 있지 않다면, 오른쪽 끝 문자를 l_stack으로 이동
        if len(r_stack) >= 1:
            l_stack.append(r_stack.pop())

    # "B" 명령어: 커서 왼쪽 문자 삭제 (Backspace)
    elif command[0] == 'B':
        # l_stack이 비어 있지 않다면, 왼쪽 끝 문자를 삭제
        if len(l_stack) >= 1:
            l_stack.pop()

    # "P x" 명령어: 커서 왼쪽에 문자 x 삽입
    elif command[0] == 'P':
        # l_stack에 새로운 문자 추가
        l_stack.append(command[1])

# 최종적으로 r_stack에 있는 문자들을 역순으로 뒤집어 l_stack에 추가합니다.
# 이는 커서를 기준으로 왼쪽과 오른쪽 스택을 합쳐서 최종 문자열을 만드는 과정입니다.
l_stack.extend(reversed(r_stack))

# 리스트를 문자열로 변환하여 출력합니다.
print(''.join(l_stack))