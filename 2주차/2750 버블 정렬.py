N = int(input())  # 사용자로부터 숫자의 개수를 입력 받음
numbers = [int(input()) for _ in range(N)]  # 사용자로부터 숫자들을 입력받아 리스트에 저장

# 버블 정렬(Bubble Sort) 알고리즘을 사용하여 리스트를 정렬
# 리스트의 길이 - 1 번 반복하여 정렬을 수행
# 이는 각 반복마다 가장 큰 숫자가 정렬된 위치로 이동하기 때문에 점점 반복 횟수가 줄어든다
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i): # 두번째 for루프에서 리스트를 한번 순회하여 인접한 원소들과 비교
        if numbers[j] > numbers[j + 1]:
            # 조건문에서 현재 원소와 다음 원소를 비교하여 정렬이 필요한 경우 위치를 교환한다.
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# 정렬된 숫자들을 순서대로 출력
for n in numbers:
    print(n)