import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# 상근이가 가지고 있는 카드 개수 입력
n = int(input())

# 상근이 카드 리스트 입력 받고 정렬
sangen = sorted(list(map(int, input().split())))  # 정렬은 사실 이 코드에서 필요하지 않지만, 이후 다른 방식(이진 탐색 등)에 대비했을 가능성 있음

# 찾고 싶은 카드 개수 입력
m = int(input())

# 찾고 싶은 카드 리스트 입력
cards = list(map(int, input().split()))

# 상근이 카드 개수를 세기 위한 딕셔너리 생성
dic1 = {}

# 상근이 카드 목록을 하나씩 돌면서 개수 세기
for x in sangen:
    if x in dic1:
        dic1[x] += 1  # 찾아야 하는 수가 상근이한테 있으면 계속 카운팅 하면서 동작 진행
    else:
        dic1[x] = 1   # 카운팅을 하다가 처음 본 숫자가 등장하면 동작 정지

# 찾고자 하는 카드 목록을 하나씩 돌면서 결과 출력
for y in cards:
    if y in dic1:
        print(dic1[y],end='')  # 존재하면 해당 숫자의 개수 출력
    else:
        print(0,end='')        # 존재하지 않으면 0 출력