import sys
input = sys.stdin.readline
# import sys와 input = sys.stdin.readline은 입력을 표준 입력에서 한 줄씩 받기 위한 설정입니다.

N = int(input())
# N = int(input())은 입력으로 들어오는 숫자의 개수를 읽습니다.

count = [0] * 10001
# count = [0] * 10001은 숫자의 등장 횟수를 저장할 리스트를 생성합니다. 여기서 10001은 입력될 수 있는 숫자의 범위를 나타냅니다 (0부터 10000까지의 숫자).

for _ in range(N):
    num = int(input()) # 숫자를 입력 받게 함
    count[num] += 1 # for _ in range(N):에서는 입력받은 숫자를 하나씩 읽어와서 count 배열에 해당 숫자의 등장 횟수를 기록합니다.

# for i in range(10001):에서는 count 배열을 처음부터 끝까지 순회합니다.
for i in range(10001):
    if count[i] != 0: #if count[i] != 0: 조건은 숫자 i가 등장한 횟수가 0이 아닌 경우에만 아래의 반복문을 실행합니다.
        for j in range(count[i]):
            # for j in range(count[i]):에서는 숫자 i를 count[i] 만큼 출력합니다. 이는 i가 몇 번 등장했느냐에 따라 그만큼 출력됩니다.
            print(i)