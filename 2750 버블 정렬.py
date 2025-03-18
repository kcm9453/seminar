N = int(input())  # 정수 N 입력받기
numbers = [int(input()) for _ in range(N)]  # 리스트에 N개의 숫자 입력받기

# 올바른 버블 정렬 구현
for i in range(len(numbers) - 1):  # 리스트 크기 - 1 만큼 반복 , (외부루프), 리스트의 길이가 n일때 n-1번씩 반복
    for j in range(len(numbers) - 1 - i):  # 앞쪽 요소와 바로 다음 요소를 비교 (내부루프),
        if numbers[j] > numbers[j + 1]:  # 앞쪽 숫자가 더 크면 교환
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# 정렬된 리스트 출력
for n in numbers:
    print(n)