N = int(input())  # 숫자의 개수를 입력받음
numbers = [int(input()) for _ in range(N)]  # 숫자들을 리스트에 입력받음

# 버블 정렬(Bubble Sort) 알고리즘을 사용하여 리스트를 정렬
# 리스트의 길이 - 1 번 반복하여 정렬을 수행
for i in range(len(numbers) - 1):
    # 각 반복마다 현재 원소와 그 다음 원소를 비교하여 정렬
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            # 인접한 두 원소를 비교하여 순서가 뒤바뀌어 있다면 서로 위치를 변경
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# 정렬된 숫자들을 순서대로 출력
for n in numbers:
    print(n)